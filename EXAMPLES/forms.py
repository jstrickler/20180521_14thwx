#!/usr/bin/env python
# (c)2015 John Strickler
from flask_wtf import Form
import re

from wtforms import (
    StringField, SubmitField, BooleanField, DateField,
    DecimalField, IntegerField, RadioField,
    SelectField, PasswordField
)
from wtforms.validators import InputRequired, Regexp, Optional

class NameForm(Form):
    name = StringField(
        "Knight name?",
        validators=[
            InputRequired(message="Knight's name must be specified"),
            Regexp(
                r'[A-Z][a-z]{3,}',
                re.IGNORECASE,
                'Name must start with a capital letter and be at least 4 letters long'
            ),
        ]
    )
    quest = StringField("And what is your quest?", validators=[Optional()], default='the Grail')
    submit = SubmitField('Off you go!')

class DemoForm(Form):
    name = StringField("Your name")
    programmer = BooleanField("Are you a programmer?")
    start_date = DateField("When can you start?")
    cost_per_hour = DecimalField("Hourly rate", places=2)
    hours_per_week = IntegerField("How many hours per week?")
    secret_word = PasswordField("What's the secret word?")
    submit = SubmitField('SEE DEMO')

