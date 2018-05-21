#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

app = Flask(__name__)

def _python_to_camelcase(s):
    return s.title().replace('_', '')

app.jinja_env.filters['pytocam'] = _python_to_camelcase

@app.route('/')
def index():
    return render_template(
        'custom_filter.html',
        function='this_is_only_a_test'
    )

if __name__ == '__main__':
    app.run(debug=True)
