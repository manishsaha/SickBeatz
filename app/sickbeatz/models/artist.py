from . import *

class Artist(Base):
  __tablename__ = 'artists'

  name          = db.Column(db.String(128), nullable =False)
  genre         = db.Column(db.String(128), nullable =False)

  def __init__(self, **kwargs):
    self.name     = kwargs.get('name', None)
    self.genre    = kwargs.get('genre', None)

  def __repr__(self):
    return str(self.__dict__)
