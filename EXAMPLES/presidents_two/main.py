#!/usr/bin/env python
# (c)2015 John Strickler
from models import President
from EXAMPLES.presidents_two import create_app

app = create_app()

@app.route('/')
def index():
    return "<h1>Try /president/#</h1>"

# @app.route('/initdb')
# def initdb():
#     db.create_all()
#     return("<h1>Database initialized</h1>")


@app.route('/president/<int:termnum>')
def show_pres(termnum):
    p = President.query.filter(President.num == termnum).first()
    if p:
        html = '<html><head><title>President #{}</title></head><body>'.format(termnum)
        html += 'President #{}<br/>\n'.format(termnum)
        html += 'Name: {} {}<br/>\n'.format(p.fname, p.lname)
        html += 'Lived: {} to {}<br/>\n'.format(p.dbirth, p.ddeath)
        html += 'Born in: {}, {}<br/>\n'.format(p.birthplace, p.birthstate)
        html += 'Served: {} to {}<br/>\n'.format(p.dstart, p.dend)
        html += 'Party: {}<br/>\n'.format(p.party)
        html += '</body></html>'

        return html, 200
    else:
        return "No such president", 200

if __name__ == '__main__':
    app.run(debug=True)


