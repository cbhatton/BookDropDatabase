from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, validators
from wtforms.widgets import NumberInput  # type: ignore


class ReviewForm(FlaskForm):

   user_name = StringField("User Name")
   star_rating = IntegerField(
        "Star Rating", [validators.NumberRange(min=0, max=5)], default=0,
        widget=NumberInput(min=0, max=5, step=1))
   location = IntegerField(
        "Location (area code)", [validators.NumberRange(min=0, max=999)], default=0)
