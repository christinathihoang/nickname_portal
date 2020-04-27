from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())


login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app) 

from app.models import User, Submission

admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Submission, db.session))

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


from app import routes, models