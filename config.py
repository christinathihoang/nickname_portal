import os

class Config(object):
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  DATABASE_URL='postgresql://christinahoang:kappas1995@localhost:5432/nickname_portal'