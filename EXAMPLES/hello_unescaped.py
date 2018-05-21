#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request, Markup

app = Flask(__name__)

MESSAGE = '''<h3>The Three Weapons of the Spanish Inquisition</h3>
<ul>
<li>Fear</li>
<li>Surprise</li>
<li>Ruthless Efficiency</li>
</ul>
'''

@app.route('/')
def index():
    return render_template(
        'hello_unescaped.html',
        markup=Markup(MESSAGE),
        message=MESSAGE,
    )

if __name__ == '__main__':
    app.run(debug=True)
