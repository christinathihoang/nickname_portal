from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
  username = StringField('Username') #need to input DataRequired() validator later, DataRequired having issues with being imported 
  password = StringField('Password')
  submit = SubmitField('Sign In')


class NicknameSubmissionForm(FlaskForm):
	 nickname = StringField('Nickname')
	 meaning = StringField('Mearning')
	 submit = SubmitField('Submit Nickname')
