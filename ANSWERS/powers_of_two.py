#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    page = '<h1>Powers of two </h1>\n'
    for i in xrange(32):
        line = '2^{0} = {1}<br/>\n'.format(i, 2**i)
        page += line
    return page


if __name__ == '__main__':
    app.run(debug=True)
