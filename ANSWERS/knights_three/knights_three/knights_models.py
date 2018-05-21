#!/usr/bin/env python
# (c)2015 John Strickler
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Knight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    title = db.Column(db.String(32))
    color = db.Column(db.String(32))
    quest = db.Column(db.String(32))
    comment = db.Column(db.String(128))

    def __repr__(self):
        return '<{} {}>'.format(self.title, self.name)
