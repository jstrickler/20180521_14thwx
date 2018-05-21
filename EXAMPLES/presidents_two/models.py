#!/usr/bin/env python
# (c)2015 John Strickler
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class President(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    dbirth = db.Column(db.Date())
    ddeath = db.Column(db.Date())
    birthplace = db.Column(db.String(80))
    birthstate = db.Column(db.String(80))
    dstart = db.Column(db.Date())
    dend = db.Column(db.Date())
    party = db.Column(db.String(32))

    def __repr__(self):
        return '<President {} {}>'.format(self.fname, self.lastname)

