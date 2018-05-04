from . import *

def get_users():
  return User.query.all()

def get_user_id(idd):
  return User.query.filter_by(id = idd).first()

def get_user_name(name):
  return User.query.filter_by(name = name).first()

def add_user(usr):
  db.session.add(usr)
  db.session.commit()
  return usr

def delete_user(usr):
  elt = User.query.filter_by(id = usr.id).first()
  if elt:
    db.session.delete(elt)
    db.commit()
    return True
  else:
    return False

def delete_users():
  User.query.delete()
  db.commit()
  return True