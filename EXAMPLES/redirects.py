#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    html =  "<h1>Home is where the heart is</h1>"
    html += "Try .../obsolete<br/>"

    return html


@app.route('/obsolete')
def old_page():
  # Second param specifies type of redirect
  return redirect('/', 301)

if __name__ == '__main__':
    app.run(debug=True)


