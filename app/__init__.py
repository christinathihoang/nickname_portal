from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())


login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)


# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


from app import routes, models