#!/usr/bin/env python
# (c)2015 John Strickler
from datetime import date

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from forms import NameForm, DemoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My hovercraft is full of eels'
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    quest = None
    name_form = NameForm()
    if name_form.validate_on_submit(): # when user presses "Submit"
        name = name_form.name.data
        quest = name_form.quest.data
        # do the business logic with the data the user put into the name_form
        name_form.name.data = ''
        name_form.quest.data = ''
    return render_template('indexform.html', form=name_form, name=name, quest=quest)


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    demo_form = DemoForm()
    if demo_form.validate_on_submit():
        # process demo_form data here....
        demo_form.name = ''
        demo_form.programmer = False
        demo_form.start_date = ""
        demo_form.hours_per_week = 0
        demo_form.cost_per_hour = 0
        demo_form.secret_word = ''
        return render_template(
            'demoform.html',
            form=demo_form,
        )
    else:
        demo_form.start_date = str(date.today())
        
        return render_template(
            'demoform.html',
            form=demo_form,
        )

if __name__ == '__main__':
    app.run(debug=True)
