#!/usr/bin/env python3
# (c) 2015 John Strickler
#
from flask import Flask
from models import db, President


def create_app():
    app = Flask(__name__)

    # in Real Life, get from config or file or environment
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:scripts@localhost/postgres'

    db.init_app(app)

    return app
