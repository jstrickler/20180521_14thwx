#!/usr/bin/env python
# (c)2015 John Strickler
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>HTTP Responses</h1>
        <h2>Try:</h2>
        <h2>/str/</h2>
        <h2>/obj/</h2>
        <h2>/tuple/</h2>
    '''

@app.route('/str/')
def return_str():
    return("<h1>String</h1>")

@app.route('/obj/')
def return_obj():
    return make_response(
        ('<h1>Response object</h1>')
    )

@app.route('/tuple/')
def return_tuple():
    return "<h1>Tuple</h1>", 200, { 'Content-type': 'text/html'}

@app.route('/show')
def show_request_context():
    html = ""
    for attr in sorted(dir(request)):
        html += "{}: {}<br/>\n".format(attr, getattr(request, attr))

    html += "<hr/>\n"
    html += str(request.user_agent) + '<br/>'

    return html







if __name__ == '__main__':
    app.run(debug=True)
