#!/usr/bin/env python
# (c) 2015 John Strickler
'''
Blueprints for display a list of knights, or an individual knight from a database
'''
from flask import Blueprint, render_template, abort

from knights_models import Knight

knights = Blueprint('knights', __name__)

@knights.route('/')
def knight_list():
    knights_list = Knight.query.all()
    return render_template('knight_list.html', title="Knights of the Round Table", knights=knights_list)


@knights.route('/knight/<name>')
def knight_by_name(name):
    knight = Knight.query.filter_by(name=name).first()
    if knight:
        return render_template('knight_view.html', title="{} {}".format(knight.title, knight.name), knight=knight)
    else:
        return '<h1>NOT FOUND</h1>'
