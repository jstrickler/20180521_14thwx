#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request
from jinja_tests import _safe_for_oysters
app = Flask(__name__)

months = '''January February March April May June July August
September October November December'''.split()

app.jinja_env.tests['okforoysters'] = _safe_for_oysters

@app.route('/')
def index():
    return render_template(
        'custom_test.html',
        months=months,
    )

if __name__ == '__main__':
    app.run(debug=True)
