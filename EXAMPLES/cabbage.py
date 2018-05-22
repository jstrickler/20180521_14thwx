#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '''<h1>url_for() demo</h1>
    <h2><a href="{}">Page 1</a></h2>
    <h2><a href="{}">Page 2</a></h2>
    '''.format('/stuff/page1', url_for('page2'))

@app.route('/stuff/page1')
def page1():
    return """
    <h1>Page 1</h1>
    <h3><a href="{}">Return to main page</a></h3>
    """.format(url_for('index'))

@app.route('/stuff/page2')
def page2():
    return """
    <h1>Page 2</h1>
    <h3><a href="{}">Return to main page</a></h3>
    """.format(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
