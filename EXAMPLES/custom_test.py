#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

app = Flask(__name__)

months = '''January February March April May June July August
September October November December'''.split()


def _safe_for_oysters(s):
    return "r" in s

app.jinja_env.tests['okforoysters'] = _safe_for_oysters

@app.route('/')
def index():
    return render_template(
        'custom_test.html',
        months=months,
    )

if __name__ == '__main__':
    app.run(debug=True)
