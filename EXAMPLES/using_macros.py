#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'using_macros.html',
    )

if __name__ == '__main__':
    app.run(debug=True)
