#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, render_template, request

app = Flask(__name__)

def py_to_cam(s):
    return s.title().replace('_', '')

app.jinja_env.filters['pytocam'] = py_to_cam

@app.route('/')
def index():
    return render_template(
        'custom_filter.html',
        movie = 'a_boy_and_his_dog',
        function='this_is_only_a_test'
    )

if __name__ == '__main__':
    app.run(debug=True)
