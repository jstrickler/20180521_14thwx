#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>HTTP Response Objects</h1>
        <h2>Try:</h2>
        <h2>/obj/username</h2>
    '''


@app.route('/obj/<username>')
def return_obj(username):
    resp = make_response(
        ('<h1>Response object</h1>', 200, { 'Content-type': 'text/html' })
    )
    resp.set_cookie('username', username)

    return resp

if __name__ == '__main__':
    app.run(debug=True)
