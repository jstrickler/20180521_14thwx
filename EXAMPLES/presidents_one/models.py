#!/usr/bin/env python
# (c)2015 John Strickler
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class President(db.Model):
    __tablename__ = 'presidents'

    id = db.Column(db.Integer, primary_key=True)
    termnum = db.Column(db.Integer)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    birthdate = db.Column(db.Date())
    deathdate = db.Column(db.Date())
    birthplace = db.Column(db.String(80))
    birthstate = db.Column(db.String(80))
    termstart = db.Column(db.Date())
    termend = db.Column(db.Date())
    party = db.Column(db.String(32))

    def __repr__(self):
        return '<President {} {}>'.format(self.fname, self.lastname)

