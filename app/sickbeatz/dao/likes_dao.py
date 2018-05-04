from . import *

def all_likers(artist):
  _id = artist.id
  idlst = Like.query(user_id).filter_by(artist_id = _id).all()
  usrlst = []
  for usrid in idlst:
    usr = users_dao.get_user_id(usrid)
    usrlst.append(usr)
  return usrlst

def all_likings(user):
  _id = user.id
  idlst = Like.query(artist_id).filter_by(user_id = _id).all()
  artistlst = []
  for artistid in artistlst:
    artist = get_artist_id(artistid)
    artistlst.append(artist)
  return artistlst

def add_like(artist, user):
  new_like = Like(artist_id = artist.id, user_id = user.id)
  db.session.add(new_like)
  db.session.commit()
  return new_like

def delete_like(artist, user):
  elt = Like.query.filter_by(artist_id = artist.id, user_id = user.id).first()
  if elt:
    db.session.delete(elt)
    db.session.commit()
    return True
  else:
    return False

def delete_likes(user):
  elts = Like.query.filter_by(user_id = user.id).all()
  for elt in elts:
    db.session.delete(elt)
  db.session.commit()
  return True