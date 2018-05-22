#!/usr/bin/env python
# (c)2015 John Strickler
from random import randint
from flask import Flask, render_template, request

app = Flask(__name__)

FRUITS = ["apple", "banana", "mango", "fig", "muskmelon"]


@app.route('/')
def index():
    data = {
        'username': 'Bob',
        'number': randint(1, 50),
        'fruits': FRUITS,
    }
    
    return render_template(
        'control_structures.html',
        **data  # unpact dict into named params
    )

if __name__ == '__main__':
    app.run(debug=True)
