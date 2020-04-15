from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user

 
from app import app, db
from app.forms import RegistrationForm, LoginForm, NicknameSubmissionForm
from app.models import User, Sister, Base
from app.create_db import session

import uuid 

Base.query = session.query()   # allow flask to access User tables

@app.route('/')
def index():
  return "Kappa Submisson Portal"


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  email = form.email.data
  password = form.password.data

  if form.validate_on_submit():

    existing = session.query(User).filter_by(email=email).first()

    if existing:
      return redirect(url_for('login'))

    user = User(id=uuid.uuid1().hex,email=email)
    user.set_password(password)

    session.add(user)
    session.commit()
    return redirect(url_for('index'))

  return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:   # if user is already logged in, then they can't go back to login page
    return redirect(url_for('/'))
    
  form = LoginForm()
  if form.validate_on_submit():   #if form is empty, returns false and renders template
    user = User.query.filter_by(email=form.email.data).first()    # search db for user by email

    if user is None or not user.check_password(form.password.data):
      flash('You are not registered')
      return redirect(url_for('/'))

    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('index'))
    # !!!!!! NEED TO IMPLEMENT CODE TO VALIDATE NEXT PARAMETER!!!
    # next = flask.request.args.get('next')
    #     # is_safe_url should check if the url is safe for redirects.
    #     # See http://flask.pocoo.org/snippets/62/ for an example.
    #     if not is_safe_url(next):
    #         return flask.abort(400)

    #     return flask.redirect(next or flask.url_for('index'))
  return render_template('login.html', form=form)

@app.route('/submission')
def submission():
	form = NicknameSubmissionForm()
	return render_template('submission.html', form=form)

@app.route('/search')
def search():
  sisters = session.query(Sister).all()
  return render_template('search.html', sisters=sisters)

@app.route('/users')
def users():
  users = session.query(User).all()
  return render_template('users.html', users=users)