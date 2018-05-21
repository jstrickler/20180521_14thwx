#!/usr/bin/env python
# (c)2015 John Strickler

from random import randint

from flask_bootstrap import Bootstrap
from flask import Flask, render_template

from president import President

app = Flask(__name__)
Bootstrap(app)

FRUITS = ["apple", "banana", "mango", "fig", "muskmelon"]


@app.route('/')
def index():
    return render_template(
        'bootstrap_hello.html',
        fruits=FRUITS,
        number=randint(1, 50),
    )


@app.route('/presidents/')
def list_presidents():
    """Return list of all presidents"""
    presidents = []
    for i in xrange(1, 45):
        presidents.append(President(i))
    return render_template('president_list_bs.html', presidents=presidents)


if __name__ == '__main__':
    app.run(debug=True)
