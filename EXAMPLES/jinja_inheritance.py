#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, render_template

from president import President

app = Flask(__name__)


@app.route('/')
def index():
    """Default page for this site"""
    return '''
    <h2>try ...</h2>
    <h3>/president/#</h3>
    <h3>/president/name</h3>
    <h3>/presidents</h3>
    '''


@app.route('/president/<int:termnum>/')
def president_by_term(termnum):
    """Retrieve president information for a specified term number"""
    term = int(termnum)
    if 0 < term < 45:
        p = President(term)
        return render_template('president_detail.html', presidents=[p])
    else:
        return '<h2>Sorry,  {} is not a valid term number</h2>'.format(term)

@app.route('/president/<last_name>/')
def president_by_last_name(last_name):
    """Retrieve president information for a specified last name;
        May return info for more than one president
    """
    presidents = []
    for i in xrange(1, 45):
        p = President(i)
        if p.last_name.lower() == last_name.lower():
            presidents.append(p)

    if presidents:
        return render_template('president_results.html', presidents=presidents)
    else:
        return '<h2>Sorry,  {} not found</h2>'.format(last_name)

@app.route('/presidents/')
def list_presidents():
    """Return list of all presidents"""
    presidents = []
    for i in xrange(1, 45):
        presidents.append(President(i))
    return render_template('president_list.html', presidents=presidents)

if __name__ == '__main__':
    app.run(debug=True)
