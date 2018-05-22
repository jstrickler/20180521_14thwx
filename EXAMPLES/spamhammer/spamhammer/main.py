#!/usr/bin/env python
# (c)2015 John Strickler

import os
from flask import Flask

DEBUG = bool(os.getenv('FLASK_DEBUG', True))


if DEBUG:
    from config import DevelopmentConfig as CONFIG
else:
    from config import ProductionConfig as CONFIG

app = Flask(__name__)
app.config.from_object(CONFIG)


@app.route('/')
def index():
    return '<h1>Welcome to SpamHammer!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
