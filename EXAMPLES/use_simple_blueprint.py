#!/usr/bin/env python3
# (c) 2015 John Strickler


from flask import Flask
from simple_blueprint import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

if __name__ == '__main__':
    app.run(debug=True)
