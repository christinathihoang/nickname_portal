import sys
import os

from app import app, db
from config import Config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()

class User(Base):
  __tablename__="users"
  id = Column(String, primary_key=True)
  username = Column(String)
  email = Column(String)
  passwordHash = Column(String)

  def __repr__(self):
        return '<User {}>'.format(self.username)

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