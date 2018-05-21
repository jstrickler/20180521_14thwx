#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>HTTP Error Handling</h1>
        <h2>Try:</h2>
        <h2>/404/</h2>
        <h2>/410/</h2>
        <h2>/500/</h2>
    '''

@app.route('/<int:error_code>/')
def simulate_error(error_code):
    code = int(error_code)
    abort(code)

@app.errorhandler(404)
def not_found(err):
    return render_template('generic_error.html', error_type="Not Found",
           error_message="Sorry, but we can't find what you were looking for"), 404

@app.errorhandler(410)
def page_gone(err):
    return render_template('generic_error.html', error_type="Gone",
           error_message="Sorry, but that page is gone for good."), 404


@app.errorhandler(500)
def app_error(err):
    return render_template('generic_error.html', error_type="Application Error",
           error_message="Sorry, but something unexpected happened on our end."), 404

if __name__ == '__main__':
    app.run(debug=True)

