from flask import Flask, render_template
from app import app
from app.forms import LoginForm, NicknameSubmissionForm

@app.route('/')

@app.route('/index')
def index():
  form = LoginForm()
  return render_template('login.html', form=form)

@app.route('/submission')
def submission():
	form = NicknameSubmissionForm()
	return render_template('submission.html', form=form)