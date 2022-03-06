from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired


class ImageForm(Form):
    image = FileField('image', [FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    title = StringField('title', [InputRequired()])
