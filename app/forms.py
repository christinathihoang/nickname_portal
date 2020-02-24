from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

class LoginForm(FlaskForm):
  username = StringField('Username') #need to input DataRequired() validator later, DataRequired having issues with being imported 
  password = StringField('Password')
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')


class NicknameSubmissionForm(FlaskForm):
	 nickname = StringField('Nickname')
	 meaning = StringField('Mearning')
	 submit = SubmitField('Submit Nickname')
