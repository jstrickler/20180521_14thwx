#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return login_user()
    else:
        return show_login_page()


@app.route('/president/new', methods=['POST'])
def add_president():
    return("<h3>President added</h3>")


@app.route('/president/<int:term_number>', methods=['PUT'])
def put_president(term_number):
    return("<h3>President {} updated</h3>".format(term_number))


@app.route('/president/<int:term_number>', methods=['DELETE'])
def delete_president(term_number):
    return("<h3>President #{} deleted</h3>".format(term_number))


def show_login_page():
    return "<h1>Please log in</h1>"

def login_user():
    return "<h1>Logging in....</h1>"


if __name__ == '__main__':
    app.run(debug=True)
