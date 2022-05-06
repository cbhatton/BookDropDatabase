from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, validators
from wtforms.widgets import NumberInput  # type: ignore


class BookForm(FlaskForm):

    book_name = StringField("Book Name", [validators.Length(min=1)])
    author_name = StringField("Author Name", [validators.Length(min=1)])
    # user_name = StringField("User Name")
    # star_rating = IntegerField(
    #     "Star Rating", [validators.NumberRange(min=0, max=5)], default=0,
    #     widget=NumberInput(min=0, max=100, step=1))
