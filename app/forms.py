from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class RegistrationForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

  # def validate_email(self, email):
  #   user = User.query.filter_by(email=email.data).first()
  #   if user is not None:
  #     raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  password = StringField('Password')
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')


class NicknameSubmissionForm(FlaskForm):
	 nickname = StringField('Nickname')
	 meaning = StringField('Mearning')
	 submit = SubmitField('Submit Nickname')
