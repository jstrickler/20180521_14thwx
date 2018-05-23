#!/usr/bin/env python3
# (c) 2015 John Strickler
#

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_caching import Cache
app = Flask(__name__)
app.secret_key = 'some_secret'

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/')
def index():
    return render_template('flash_index.html')

cache.cached(timeout=3600)
@app.route('/popular/<float:lat>/<float:long>')
def popular_view(lat, long):
    return "Something using lat and long..."

# @app.before_request
# def blacklist(request):
#     if request.ip == '123.4.56.78':
#         redirect('/baduser', 403)

@app.after_request
def downgrade_heading(response):
    response.data = response.data.replace('h1', 'h3') 
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('flash_login.html', error=error)

if __name__ == "__main__":
    app.run()



