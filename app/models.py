import sys
import os

from app import app, db, login
from config import DevelopmentConfig

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
 
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

SQLALCHEMY_DATABASE_URI = 'postgresql://christinahoang:kappas1995@localhost:5432/nickname_portal'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

class User(UserMixin, Base):
  __tablename__= 'users'

  id = Column(String, primary_key=True, nullable=False)
  email = Column(String, nullable=False)
  password_hash = Column(String, nullable=False)
  authenticated = Column(Boolean, default=True)

  def __repr__(self):
    return '<User {}>'.format(self.id)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

# This callback is used to reload the user object from the user ID stored in the session
@login.user_loader
def load_user(id):
  return session.query(User).get((id))


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

Base.metadata.drop_all(engine)    # drops all existing tables
Base.metadata.create_all(engine)  # creates new tables