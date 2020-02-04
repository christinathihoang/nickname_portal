from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SubmissionForm(FlaskForm):
	 nickname = StringField('nickname')
	 meaning = StringField('meaning')
	 submit = SubmitField('submit nickname')