#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return_str = '''<h1>Query strings demo</h1>\n'''
    for query_name, query_value in request.args.iteritems():
        return_str += '{} => {}<br/>\n'.format(query_name, query_value)

    return return_str


if __name__ == '__main__':
    app.run(debug=True)
