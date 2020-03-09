import json, logging

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from app.models import Base, User, Sister, engine


Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()


def load_json(filename):
  with open(filename) as file:
    jsn = json.load(file)
    file.close()
  return jsn


def create_sister():
  sisters = load_json('app/static/sister_info.json')
  for sister in sisters:
    try:
      nickname = sister['nickname']
      firstname = sister['firstname']
      lastname = sister['lastname']
      sclass = sister['class']
      semester = sister['semester']
      year = sister['year']
      linenumber = sister['linenumber']
      chapter = sister['chapter']
    except IntegrityError:
      pass

    newSister = Sister(nickname=nickname,firstname=firstname,lastname=lastname,chapter=chapter,sclass=sclass,semester=semester,year=year,linenumber=linenumber)
    
    session.add(newSister)
    session.commit()

create_sister()
