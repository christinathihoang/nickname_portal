from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required

 
from app import app, db
from app.forms import RegistrationForm, LoginForm, NicknameSubmissionForm
from app.models import User, Sister, Base, session
# from app.create_db import session

import uuid 

Base.query = session.query()   # allow flask to access User tables

@app.route('/')
def index():
  if current_user.is_authenticated:   # if user is already logged in, then they can't go back to index page
    return redirect(url_for('home'))
  
  registrationForm = RegistrationForm()
  loginForm = LoginForm()
  return render_template('index.html', loginForm=loginForm, registrationForm=registrationForm)

@app.route('/home')
def home():
  return "Hello"

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:   # if user is already logged in, then they can't go back to register page
    return redirect(url_for('home'))
  
  registrationForm = RegistrationForm()
  loginForm = LoginForm()

  if registrationForm.submit.data and registrationForm.validate_on_submit():

    existing = session.query(User).filter_by(email=registrationForm.email.data).first()

    if existing:
      return redirect(url_for('login'))

    user = User(id=str(uuid.uuid1().int),email=registrationForm.email.data)
    user.set_password(registrationForm.password.data)

    session.add(user)
    session.commit()
    return redirect(url_for('login'))

  return render_template('index.html', loginForm=loginForm, registrationForm=registrationForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:   # if user is already logged in, then they can't go back to login page
    return redirect(url_for('home'))
    
  registrationForm = RegistrationForm()
  loginForm = LoginForm()

  if loginForm.submit.data and loginForm.validate_on_submit():   #if form is empty, returns false and renders template
    user = session.query(User).filter_by(email=loginForm.email.data).first()    # search db for user by email

    if user is None or not user.check_password(loginForm.password.data):
      return redirect(url_for('login'))

    login_user(user, remember=loginForm.remember_me.data)

    # redirecting user back to the page that they were originally trying to access
    next_page = request.args.get('next')
    return redirect(next_page or url_for('home'))
  return render_template('index.html', loginForm=loginForm, registrationForm=registrationForm)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   if current_user.is_authenticated:   # if user is already logged in, then they can't go back to login page
#     return redirect(url_for('index'))
    
#   loginForm = LoginForm()
#   registrationForm = RegistrationForm()

  # # REGISTRATION FORM
  # if registrationForm.submit.data and registrationForm.validate_on_submit():
  #   existing = session.query(User).filter_by(email=registrationForm.email.data).first()
  #   print('registration button clicked')

  #   if existing:
  #     return redirect(url_for('login'))

  #   user = User(id=str(uuid.uuid1().int), email=registrationForm.email.data)
  #   user.set_password(registrationForm.password.data)

  #   session.add(user)
  #   session.commit()
  #   return redirect(url_for('login'))

  # # LOGIN FORM
  # if loginForm.submit.data and loginForm.validate_on_submit():   #if form is empty, returns false and renders template
  #   user = session.query(User).filter_by(email=loginForm.email.data).first()    # search db for user by email
  #   print('Login button clicked')
  #   if user is None or not user.check_password(loginForm.password.data):
  #     return redirect(url_for('login'))

  #   # login_user(user, remember=loginForm.remember_me.data)

  #   # redirecting user back to the page that they were originally trying to access
  #   next_page = request.args.get('next')
  #   # return redirect(next_page or url_for('index'))
  #   print("redirecting")
  #   return redirect(url_for('index'))

  # return render_template('login.html', loginForm=loginForm, registrationForm=registrationForm)

@app.route('/submission')
@login_required
def submission():
	form = NicknameSubmissionForm()
	return render_template('submission.html', form=form)

@app.route('/search')
@login_required
def search():
  sisters = session.query(Sister).all()
  return render_template('search.html', sisters=sisters)

@app.route('/users')
def users():
  users = session.query(User).all()
  return render_template('users.html', users=users)