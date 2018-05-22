#!/usr/bin/env python
# (c)2015 John Strickler
import logging
from flask import Flask
from flask_log import Logging

ADMINS = ['jstrickler@gmail.com']

app = Flask(__name__)
flask_log = Logging(app)

if not app.debug:

    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(('smtpcorp.com', 8025),
                               'server-error@myflaskapp.com',
                               ADMINS, "Log Entry", ('jstrickler', 'python(monty)'))
    mail_handler.setLevel(logging.CRITICAL)
    app.logger.addHandler(mail_handler)

    from logging import FileHandler
    file_handler = FileHandler('flaskapp.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
else:
    print "Wah-wah"

@app.route('/')
def index():
    return '''<h1>Logging</h1>
    <h3>Try .../error</h3>
    <h3>Try .../warn</h3>
    <h3>Try .../critical</h3>
    <h3>Try .../debug</h3>
    '''

@app.route('/error')
def logerror():
    app.logger.error("Error Event")
    return "<h2>error</h2>"

@app.route('/warn')
def logwarn():
    app.logger.warn("Warning Event")
    return "<h2>warn</h2>"

@app.route('/critical')
def logcritical():
    app.logger.critical("Critical Event")
    return "<h2>critical</h2>"

@app.route('/debug')
def logdebug():
    app.logger.debug("Debug Event")
    return "<h2>debug</h2>"


if __name__ == '__main__':
    app.run(debug=True)

