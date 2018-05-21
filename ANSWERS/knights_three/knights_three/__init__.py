#!/usr/bin/env python
# (c) 2015 John Strickler
from flask import Flask
from knightsviews import knights
from knights_models import db

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    db.init_app(app)
    app.register_blueprint(knights)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
