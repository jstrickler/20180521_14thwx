#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>HTTP Tuple Responses</h1>
        <h2>Try:</h2>
        <h2>.../good/</h2>
        <h2>.../bad/</h2>
        <h2>.../status/CODE</h2>
        <h2>.../html/</h2>
        <h2>.../plain/</h2>
    '''

@app.route('/good/')
def return_good():
    return ("<h1>Hello world -- all is peachy</h1>", 200)

@app.route('/bad/')
def return_bad():
    return ("<h1>Hello world -- we're doomed</h1>", 400)

@app.route('/status/<int:code>')
def return_status(code):
    return ("<h1>Hello world: status is {}</h1>".format(code), code)

@app.route('/html/')
def return_html():
    return ("<h1>Hello world -- all is peachy</h1>", 200, { 'content-type': 'text/html'})

@app.route('/plain/')
def return_plain():
    return ("<h1>Hello world -- all is peachy</h1>", 200, { 'content-type': 'text/plain'})


if __name__ == '__main__':
    app.run(debug=True)
