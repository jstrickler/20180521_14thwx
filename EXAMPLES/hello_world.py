#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, Flask world!</h1>'


@app.route('/barf')
def barf():
    return '<h1>Wow this is ugly!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
