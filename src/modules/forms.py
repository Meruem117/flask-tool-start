from wtforms import Form, FileField
from flask_wtf.file import FileAllowed, FileRequired


class ImageForm(Form):
    image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
