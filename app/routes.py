from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user

from app import app
from app.forms import LoginForm, NicknameSubmissionForm
from app.models import User, Sister
from app.create_db import session

@app.route('/')
def index():
  return "Kappa Submisson Portal"

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:   # if user is already logged in, then they can't go back to login page
    return redirect(url_for('/'))
  form = LoginForm()
  if form.validate_on_submit():   #if form is empty, returns false and renders template
    login_user(user)
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
    # !!!!!! NEED TO IMPLEMENT CODE TO VALIDATE NEXT PARAMETER!!!
    # next = flask.request.args.get('next')
    #     # is_safe_url should check if the url is safe for redirects.
    #     # See http://flask.pocoo.org/snippets/62/ for an example.
    #     if not is_safe_url(next):
    #         return flask.abort(400)

    #     return flask.redirect(next or flask.url_for('index'))
  return render_template('login.html', form=form)

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(somewhere)


# @app.route('/login2', methods=['GET', 'POST'])
# def login2():
#   form = LoginForm()
#   if form.validate_on_submit():   #if form is empty, returns false and renders template
#     flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
#     return redirect(url_for('index'))
#   return render_template('login2.html', form=form)


@app.route('/submission')
def submission():
	form = NicknameSubmissionForm()
	return render_template('submission.html', form=form)

@app.route('/search')
def search():
  sisters = session.query(Sister).all()
  return render_template('search.html', sisters=sisters)