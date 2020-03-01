from flask import Flask, render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, NicknameSubmissionForm
from app.models import Sister
from app.create_db import session

@app.route('/')
def index():
  return "Kappa Submisson Portal"

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():   #if form is empty, returns false and renders template
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
  return render_template('login.html', form=form)

@app.route('/submission')
def submission():
	form = NicknameSubmissionForm()
	return render_template('submission.html', form=form)

@app.route('/search')
def search():
  sisters = session.query(Sister).all()
  return render_template('search.html', sisters=sisters)