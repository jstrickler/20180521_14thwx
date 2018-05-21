#!/usr/bin/env python
# (c) 2015 John Strickler
'''
Blueprints for display a list of knights, or an individual knight from the knights.txt file
'''
from flask import Blueprint, render_template
from knight import Knight

knights = Blueprint('knights', __name__)

@knights.route('/')
def knight_list():
    knights = [ Knight(n) for n in Knight.get_knight_names() ]
    return render_template('knight_list.html', title="Knights of the Round Table", knights=knights)

@knights.route('/knight/<name>')
def knight_by_name(name):
    knight = Knight(name)
    return render_template('knight_view.html', title="{} {}".format(knight.title, knight.name), knight=knight)

