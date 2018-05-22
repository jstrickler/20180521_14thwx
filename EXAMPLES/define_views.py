#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask

from president import President

app = Flask(__name__)

@app.route('/')
def index():
    """Default page for this site"""
    return '''<h1>Hello, Flask world!</h1>
    <h2>try .../president/#</h1>
    '''

# http://foo.bar.com/president/1
@app.route('/president/', defaults={'termnum': None})
@app.route('/president/<int:termnum>/', methods=['GET'])
def president_by_term(termnum):
    """Retrieve president information for a specified term number"""
    if termnum is None:
        return "Please specify a president by term or last name"
    
    if 0 < termnum < 46:
        return format_html_for_president(termnum)
    else:
        html_content = '<h2>Sorry,  {} is not a valid term number</h2>'.format(termnum)
    return html_content

# http:wx.foo.com/wx/get_forecast/2018/5/25

@app.route('/wx/get_forecast/<int:year>/<int:month>/<int:day>')
def get_forecast(year, month, day):
    return ""

@app.route('/president/<last_name>/')
def president_by_last_name(last_name):
    """Retrieve president information for a specified last name;
        May return info for more than one president
    """
    html_content = ''
    for i in xrange(1, 45):
        p = President(i)
        if p.last_name.lower().startswith(last_name.lower()):
            html_content += format_html_for_president(i)

    if html_content:
        return html_content
    else:
        return '<h2>Sorry,  {} not found</h2>'.format(last_name)

@app.route('/spam')
def spam():
    return "SPAM for the win!", 400, {'X-APPLICATION-WEATHER': '14ws'}

def format_html_for_president(term_num):
    """Return HTML for one president"""
    p = President(term_num)
    return  '''
    <h1>{}: {} {}</h1>
    <h2>Born in: {}</h2>
    <h2>Lived: {} to {}</h2>
    <h2>Party: {}</h2>
    '''.format(
        term_num, p.first_name, p.last_name, p.birth_state, p.birth_date,
        p.death_date, p.party
    )


if __name__ == '__main__':
    app.run(debug=True)
