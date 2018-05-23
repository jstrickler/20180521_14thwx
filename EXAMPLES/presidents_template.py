#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, render_template, abort

from EXAMPLES.president import President

app = Flask(__name__)


@app.route('/')
def index():
    """Default page for this site"""
    return '''<h1>try .../president/#</h1>'''


@app.route('/president/<int:termnum>/')
def president_by_term(termnum):
    """Retrieve president information for a specified term number"""
    term = int(termnum)
    if 0 < term < 46:
        presidents_list = [President(term)]
        return render_template('president_results.html', presidents=presidents_list)
    else:
#        abort(404)
        html_content = '<h2>Sorry,  {} is not a valid term number</h2>'.format(term)
        return html_content, 404

@app.errorhandler(404)
def show_error_page(e):
    return render_template('404.html'), 404



# @app.errorhandler(301)
# def obsolete_handler(e):
#     return render_template('301.html'), 301

@app.route('/president/<last_name>/')
def president_by_last_name(last_name):
    """Retrieve president information for a specified last name;
        May return info for more than one president
    """
    html_content = ''
    presidents = []
    for i in xrange(1, 46):
        p = President(i)
        if p.last_name.lower() == last_name.lower():
            presidents.append(p)

    if presidents:
        return render_template('president_results.html', presidents=presidents)
    else:
        return '<h2>Sorry,  {} not found</h2>'.format(last_name)


if __name__ == '__main__':
    app.run(debug=True)
