from flask import Flask, render_template
from app import app
from app.forms import SubmissionForm

@app.route('/')

@app.route('/index')
def index():
    return "Kappa Nickname Portal"

@app.route('/submission')
def submission():
	form = SubmissionForm()
	return render_template('submission.html', form=form)