from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config())

login_manager = LoginManager(app)

db = SQLAlchemy()   # create without parameters and configure later in models.py

from app import routes, models