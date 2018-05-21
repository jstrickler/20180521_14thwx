#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>try /username/YOURNAME</h1>', 200

@app.route('/username/<username>')
def user_name(username):
    user_agent = request.headers.get('User-Agent')
    return render_template(
        'hello.html',
        browser=user_agent,
        username=username.replace('+',' '),
    )

if __name__ == '__main__':
    app.run(debug=True)
