"""
This module contains forms for the blogging app.

The primary focus is on posting comic strips, so the forms handle image files
and related metadata like title, description, and publication date.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import DateField, StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired


class ComicForm(FlaskForm):
    """
    The form will include title, description, image, date published, and submit

    """

    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    image = FileField(
        "Upload Comic", validators=[FileAllowed(["jpg", "jpeg", "png"], "Image Only!!")]
    )
    date_published = DateField("Date Published", format="%m-%d-%Y")
    submit = SubmitField("Post Comic")
