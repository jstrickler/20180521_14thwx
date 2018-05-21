#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My hovercraft is full of eels'
Bootstrap(app)

class NameForm(Form):
    name = StringField(
        "Good Sir Knight, what is your name?",
        validators=[
            DataRequired(message="Knight's named must be specified"),
            Regexp(
                r'[A-Z][a-z]{2}[a-z ]+',
                0,
                'Name must start with a capital letter and be at least 4 letters long'
            ),
        ]
    )
    quest = StringField("And what is your quest?", validators=[DataRequired()], default='the Grail')
    submit = SubmitField('Off you go!')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    quest = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        quest = form.quest.data
        form.name.data = ''
        form.quest.data = ''
    return render_template('indexform.html', form=form, name=name, quest=quest)


if __name__ == '__main__':
    app.run(debug=True)
