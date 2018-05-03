from . import *

class Artist(Base):
  __tablename__ = 'artists'

  name          = db.Column(db.String(128), nullable =False)
  genre         = db.Column(db.String(256), nullable =False)

  def __init__(self, **kwargs):
    self.name     = kwargs.get('name', None)
    self.genre    = kwargs.get('genre', None)

  def __repr__(self):
    return str(self.__dict__)

  def _urlsafe_base_64(self):
    return hashlib.sha1(os.urandom(64)).hexdigest()


class ArtistSchema(ModelSchema):
  class Meta:
    model = Artist
