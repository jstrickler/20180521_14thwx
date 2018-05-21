#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask
from sample_blueprint import sample

app = Flask(__name__)
app.register_blueprint(sample)


if __name__ == '__main__':
    app.run(debug=True)
