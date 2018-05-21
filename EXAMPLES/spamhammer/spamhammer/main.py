#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return '<h1>Welcome to SpamHammer!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
