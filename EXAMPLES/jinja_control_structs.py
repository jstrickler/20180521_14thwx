#!/usr/bin/env python
# (c)2015 John Strickler
from random import randint
from flask import Flask, render_template, request

app = Flask(__name__)

FRUITS = ["apple", "banana", "mango", "fig", "muskmelon"]


@app.route('/')
def index():
    return render_template(
        'control_structures.html',
        fruits=FRUITS,
        number=randint(1, 50),
    )

if __name__ == '__main__':
    app.run(debug=True)
