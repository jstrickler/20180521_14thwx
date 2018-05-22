#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from models import db, President

app = Flask(__name__)

# in Real Life, get from config or file or environment
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:scripts@localhost/postgres'

sqlite_db_path = '/Users/jstrick/Desktop/py2flaskintro/DATA/presidents.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///' + sqlite_db_path



db.init_app(app)

@app.route('/')
def index():
    return("<h1>Try /president/#</h1>")

# @app.route('/initdb')
# def initdb():
#     db.create_all()
#     return("<h1>Database initialized</h1>")

@app.route('/wtf')
def wtf():
    return "WTF???"

@app.route('/president/<int:termnum>/')
def show_pres(termnum):
    # select from president ....
    pres_list = President.query.filter(President.termnum == termnum)
    if pres_list:
        p = pres_list.first()
        html = '<html><head><title>President #{}</title></head><body>'.format(termnum)
        html += 'President #{}<br/>\n'.format(termnum)
        html += 'Name: {} {}<br/>\n'.format(p.firstname, p.lastname)
        html += 'Lived: {} to {}<br/>\n'.format(p.birthdate, p.deathdate)
        html += 'Born in: {}, {}<br/>\n'.format(p.birthplace, p.birthstate)
        html += 'Served: {} to {}<br/>\n'.format(p.termstart, p.termend)
        html += 'Party: {}<br/>\n'.format(p.party)
        html += '</body></html>'

        return html
    else:
        return "No such president"

if __name__ == '__main__':
    app.run(debug=True)


