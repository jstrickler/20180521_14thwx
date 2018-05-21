#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, request, g
from werkzeug.utils import escape
import animal

app = Flask(__name__)


@app.route('/')
def index():
    animal.set_animal('wombat')  # modifies g in animal module

    html = '<html><head><title>Context Objects</title></head><body>\n'

    html += '<h1>Context Objects</h1>\n'

    html += '<h2>Request Object</h2>\n'
    html += '<table border="1">\n'
    html += '<tr><th>Attribute</th><th>Object Type</th><th>Value</th></tr>\n'
    for attribute_name in dir(request):
        if not attribute_name.startswith('_'):
            attribute = getattr(request, attribute_name)
            type_name = type(attribute).__name__
            type_name = type_name if type_name else '&nbsp'
            attribute_value = escape(str(attribute))
            html += '<tr><td>{}</td><td>{!s}</td><td>{!s}</td></tr>\n'.format(attribute_name, type_name, attribute_value)

    html += '</table>\n'

    html += '<h2>g (Global) Object</h2>\n'
    html += '<table border="1">\n'
    html += '<tr><th>Attribute</th><th>Object Type</th><th>Value</th></tr>\n'
    for attribute_name in dir(g):
        if not attribute_name.startswith('_'):
            attribute = getattr(g, attribute_name)
            type_name = type(attribute).__name__
            type_name = type_name if type_name else '&nbsp'
            attribute_value = escape(str(attribute))
            html += '<tr><td>{}</td><td>{!s}</td><td>{!s}</td></tr>\n'.format(attribute_name, type_name, attribute_value)

    html += '</table>\n'

    html += '</body></html>\n'

    return html


if __name__ == '__main__':
    app.run(debug=True)
