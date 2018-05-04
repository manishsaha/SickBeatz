from user import *
from song import *
from artist import *
from like import *
from marshmallow_sqlalchemy import field_for

class UserSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = User

class SongSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Song
    
class ArtistSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Artist

class LikeSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Like

