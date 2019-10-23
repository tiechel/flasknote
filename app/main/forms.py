from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired()])
    body = TextAreaField('本文', validators=[DataRequired()])
