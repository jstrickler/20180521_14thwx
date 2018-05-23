#!/usr/bin/env python
# (c)2015 John Strickler

# use Postman to select different return types
import xml.etree.ElementTree as ET
from datetime import date

from flask import Flask, request, render_template, jsonify
from flask_bootstrap import Bootstrap

from EXAMPLES.president import President

app = Flask(__name__)
Bootstrap(app)


PRES_FIELDS = '''
    first_name last_name birth_date death_date birth_place birth_state
    term_start term_end party'''.split()


def pres_to_dict(pres):
    """Convert one president object to a dictionary"""
    pres_dict = {}
    for prop_name in dir(pres):
        if not prop_name.startswith('_'):
            prop_value = getattr(pres, prop_name)
            if isinstance(prop_value, date):
                prop_value = '{0.year:4d}-{0.month:02d}-{0.day:02d}'.format(prop_value)
            pres_dict[prop_name] = prop_value
    return pres_dict


def pres_to_xml(pres):
    p = ET.Element('president')
    for field_name in PRES_FIELDS:
        elem = ET.Element(field_name.replace('_',''))
        elem.text = str(getattr(pres, field_name))
        p.append(elem)
    return ET.tostring(p)


def pres_list_to_xml(pres_list):
    """Convert list of presidents to XML"""
    root = ET.Element('presidents')
    for pres in pres_list:
        root.append(pres_to_xml(pres))
    return ET.tostring(root)


@app.route('/')
def index():
    """Main page; returns list of all presidents"""
    presidents = []
    for i in xrange(1, 45):
        presidents.append(President(i))
    accept_type = request.headers.get('ACCEPT')
    response = ''
    print "Accept type:", accept_type
    if accept_type.startswith('text/html'):
        response = render_template('president_list_bs.html', presidents=presidents)
    elif accept_type == 'application/xml':
        response = pres_list_to_xml(presidents)
    elif accept_type == 'application/json':
        presidents_as_dicts = [pres_to_dict(p) for p in presidents]
        response = jsonify(presidents=presidents_as_dicts)
    # handle error here if non-expected type

    return response


@app.route('/president/<int:termnum>/')
def pres_by_termnum(termnum):
    accept_type = request.headers.get('ACCEPT')
    p = President(termnum)

    if accept_type == 'application/xml':
        response = pres_to_xml(p)
    else:
#     elif accept_type == 'application/json':
        president_as_dict = pres_to_dict(p)
        response = jsonify(president=president_as_dict)

    return response


if __name__ == '__main__':
    app.run(debug=True)
