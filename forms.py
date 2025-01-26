from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, DateField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class ComicForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    image = FileField(
        "Upload Comic",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png"], "Only JPG, JPEG, or PNG files are allowed!"
            )
        ],
    )
    date_published = DateField(
        "Date Published", format="%Y-%m-%d", validators=[DataRequired()]
    )
    submit = SubmitField("Post Comic")
