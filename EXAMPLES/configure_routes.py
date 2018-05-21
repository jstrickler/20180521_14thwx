#!/usr/bin/env python
# (c)2015 John Strickler
"""
Demo of route mapping
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Default page for this site"""
    return '''<h1>Welcome to our spamhammer!</h1>
    <h3>Try .../president/term</h3>
    <h3>Try .../president/lastname</h3>
    '''


@app.route('/president/term/')
def president_by_term():
    """Retrieve president information by term number"""
    return '<h1>Info for president by term</h1>'


@app.route('/president/lastname/')
def president_by_last_name():
    """Retrieve information presidents by last name"""
    return '<h1>Info for president by last name</h1>'


@app.route('/presidents/')
def list_presidents():
    """Return a list of all presidents"""
    return '<h1>List of all presidents</h1>'


if __name__ == '__main__':
    app.run(debug=True)
