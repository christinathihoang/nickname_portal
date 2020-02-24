from flask import Flask, render_template, flash, redirect
from app import app
from app.forms import LoginForm, NicknameSubmissionForm

@app.route('/')
def index():
  return "Kappa Submisson Portal"

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():   #if form is empty, returns false and renders template
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect('/')
  return render_template('login.html', form=form)

@app.route('/submission')
def submission():
	form = NicknameSubmissionForm()
	return render_template('submission.html', form=form)