#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>HTTP String Responses</h1>
        <h2>Try:</h2>
        <h2>.../plain/</h2>
        <h2>.../template/yourname</h2>
    '''

@app.route('/plain/')
def return_str():
    return("<h1>Hello world</h1>")

@app.route('/template/<username>')
def return_template(username):
    user_agent = request.headers.get('User-Agent')
    return render_template(
        'hello.html',
        browser=user_agent,
        username=username.replace('+',' '),
    )


if __name__ == '__main__':
    app.run(debug=True)
