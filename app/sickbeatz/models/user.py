from . import *

class User(Base):
  __tablename__ = 'users'

  name            = db.Column(db.String(128), nullable =False)
  email           = db.Column(db.String(128), nullable =False, unique =True)
  age             = db.Column(db.Integer, nullable=False)

  def __init__(self, **kwargs):
    self.name            = kwargs.get('name', None)
    self.email           = kwargs.get('email', None)
    self.age             = kwargs.get('age', None)

  def __repr__(self):
    return str(self.__dict__)
