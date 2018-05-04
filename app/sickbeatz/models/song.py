from . import *

class Song(Base):
  __tablename__ = 'songs'

  name   = db.Column(db.String(128), nullable =False)
  album  = db.Column(db.String(128))
  artist = db.Column(db.ForeignKey('artists.id'), nullable =False)
  uri    = db.Column(db.String(256), nullable =False)

  def __init__(self, **kwargs):
    self.name      = kwargs.get('name', None)
    self.album     = kwargs.get('album', None)
    self.artists   = kwargs.get('artist', None)
    self.uri       = kwargs.get('uri', None)

  def __repr__(self):
    return str(self.__dict__)
