from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())


login_manager = LoginManager(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return None

db = SQLAlchemy(app) 

from app.models import User, Submission, MyModelView
admin = Admin(app)

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Submission, db.session))

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


from app import routes, models