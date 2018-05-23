#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, render_template
from president import President


app = Flask(__name__)

# index = app.route('/')(index)

@app.route('/barf')
def barf():
    return '<h1>Wow this is ugly!</h1>'

@app.route('/')
def index():
    return '<div class="container">Hello, Flask world!</div>'

@app.route('/potus/<int:termnum>/')
def president_by_term(termnum):
    """Retrieve president information for a specified term number"""
    term = int(termnum)
    if 0 < term < 46:
        presidents_list = [President(term)]
        return render_template('president_results.html', presidents=presidents_list)
    else:
        html_content = '<h2>Sorry,  {} is not a valid term number</h2>'.format(term)
        return html_content, 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

