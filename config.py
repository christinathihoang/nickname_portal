import os

class DevelopmentConfig(object):
  FLASK_DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
  DATABASE_URL='postgresql://christinahoang:kappas1995@localhost:5432/nickname_portal'

class ProductionConfig(object):
  FLASK_DEBUG = False