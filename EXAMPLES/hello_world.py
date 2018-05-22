#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask


app = Flask(__name__)

# index = app.route('/')(index)

@app.route('/barf')
def barf():
    return '<h1>Wow this is ugly!</h1>'

@app.route('/')
def index():
    return '<div class="container">Hello, Flask world!</div>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

