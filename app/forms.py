from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators, ValidationError

class UploadForm(Form):
   upload = FileField('Upload Field', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
   submit = SubmitField("Send")