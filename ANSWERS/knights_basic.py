#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, url_for
from knight import Knight

app = Flask(__name__)

@app.route('/')
def index():
    page = '<h1>Knights of the Round Table</h1>\n'
    for knight in Knight.get_knight_names():
        link = '<a href="{0}">{1}</a><br/>\n'.format(
            url_for('knights', name=knight),
            knight
        )
        page += link
    return page

@app.route('/knights/<name>')
def knights(name):
    knight = Knight(name)
    return '''
    <h1>{0} {1}</h1>
    Favorite color: {2}<br/>
    Quest: {3}<br/>
    Comment: {4}<br/>
    <br/>
    <a href="{5}">return to main page</a>
    '''.format(
        knight.title,
        name,
        knight.color,
        knight.quest,
        knight.comment,
        url_for('index')
    )

if __name__ == '__main__':
    app.run(debug=True)
