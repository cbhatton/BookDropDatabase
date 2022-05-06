from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, validators
from wtforms.widgets import NumberInput  # type: ignore


class UserForm(FlaskForm):

    user_name = StringField("User Name")
    name = StringField("First Name")
