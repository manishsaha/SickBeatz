from . import *

def all_likers(artist):
  usrlst = []
  if artist:
    _id = artist.id
    idlst = db.session.query(Like.user_id).filter_by(artist_id = _id).all()
    for usrid in idlst:
      usr = users_dao.get_user_id(usrid)
      usrlst.append(usr)
  return usrlst

def all_likings(user):
  artistlst = []
  if user:
    _id = user.id
    idlst = db.session.query(Like.artist_id).filter_by(user_id = _id).all()
    for artistid in idlst:
      artist = artists_dao.get_artist_id(artistid)
      artistlst.append(artist)
  return artistlst

def add_like(artist, user):
  if artist and user:
    new_like = Like(artist_id = artist.id, user_id = user.id)
    db.session.add(new_like)
    db.session.commit()
    return new_like
  else: return None

def delete_like(artist, user):
  if user and artist:
    elt = Like.query.filter_by(artist_id = artist.id, \
      user_id = user.id).first()
    db.session.delete(elt)
    db.session.commit()
    return True
  else: return False

def delete_likes(user):
  if user:
    elts = Like.query.filter_by(user_id = user.id).all()
    for elt in elts:
      db.session.delete(elt)
    db.session.commit()
    return True
  else: return False