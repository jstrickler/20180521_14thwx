#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

from president import President

app = Flask(__name__)

FRUITS = ["apple", "banana", "mango", "fig"]


@app.route('/')
def index():
    #todo: make login prettier
    return '<h1>try /username/YOURNAME</h1>'

@app.route('/username/<username>')
def user_name(username):
    user_agent = request.headers.get('User-Agent')
    return render_template(
        'vars_and_filters.html',
        president=President(26),
        browser=user_agent,
        username=username.replace('+',' '),
        fruits=FRUITS,
    )

if __name__ == '__main__':
    app.run(debug=True)
