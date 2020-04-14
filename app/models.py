import sys
import os

from app import app, db, login_manager
from config import DevelopmentConfig

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(UserMixin, Base):
  __tablename__="users"
  id = Column(String, primary_key=True)
  email = Column(String)
  password_hash = Column(String)
  authenticated = Column(Boolean, default=True)

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  # methods for user class, required for Flask-Login
  def is_active(self):
    return True   # all users are active

  def get_id(self):
    return self.email   # return email address for Flask-Login

  def is_authenticated(self):
    return self.authenticated

  def is_anonymous(self):
    return False    # anonymous users not allowed

# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))


class Sister(Base):
  __tablename__ = "sister_info"
  nickname = Column(String, primary_key=True)
  firstname = Column(String)
  lastname = Column(String)
  chapter = Column(String)
  sclass = Column(String)
  semester = Column(String)
  year = Column(Integer)
  linenumber = Column(Integer)

#SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://christinahoang:kappas1995@localhost:5432/nickname_portal')
SQLALCHEMY_DATABASE_URI = app.config['DATABASE_URL']
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)    # drops all existing dbs
Base.metadata.create_all(engine)  # creates new dbs