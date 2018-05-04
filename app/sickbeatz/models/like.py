from . import *

class Like(Base):
  __tablename__ = 'likes'

  user_id       = db.Column(db.ForeignKey('users.id'), nullable =False)
  artist_id     = db.Column(db.ForeignKey('artists.id'), nullable =False)

  def __init__(self, **kwargs):
    self.user_id     = kwargs.get('user_id', None)
    self.artist_id   = kwargs.get('artist_id', None)

  def __repr__(self):
    return str(self.__dict__)
