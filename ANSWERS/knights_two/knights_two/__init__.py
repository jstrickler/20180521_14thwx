#!/usr/bin/env python
# (c)2015 John Strickler
"""
Main module for knights_two app
"""

from flask import Flask
from knightsviews import knights

def create_app():
    app = Flask(__name__)
    app.register_blueprint(knights)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
