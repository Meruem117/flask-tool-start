from flask_wtf import FlaskForm
from wtforms import FileField, StringField, RadioField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired


class ImageForm(FlaskForm):
    image = FileField('Image', [FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    title = StringField('Title', [InputRequired()])
    size = RadioField('Size', [InputRequired()],
                      choices=[(16, '16 * 16'), (32, '32 * 32'), (48, '48 * 48'), (64, '64 * 64'), (128, '128 * 128'),
                               (256, '256 * 256')])
