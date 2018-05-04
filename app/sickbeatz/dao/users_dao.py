from . import *

def get_user_id(idd):
  return User.query.filter_by(id = idd).first()

def get_user_name(name):
  return User.query.filter_by(name = name).first()

def add_user(usr):
  db.session.add(usr)
  db.session.commit()
  return usr