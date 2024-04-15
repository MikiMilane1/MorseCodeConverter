from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired


# WTForm for text or code input
class UserInput(FlaskForm):
    userinput = StringField(label="Enter text or Morse Code here:")
    convert_button = SubmitField(label='Convert')
    # output = StringField(label="", render_kw={'style': 'width: 80ch'})
