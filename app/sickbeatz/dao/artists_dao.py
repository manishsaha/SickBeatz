from . import *

def get_artist_name(name):
  return Artist.query.filter_by(name = name).first()

def get_artist_id(idd):
  return Artist.query.filter_by(id = idd).first()

def artists_by_name(name):
  return Artist.query.filter(Artist.name.ilike('%%%s%%', name)).all()

def get_all_artists():
  return Artist.query.all()

def add_artist(artist):
  db.session.add(artist)
  db.session.commit()
  return artist

def delete_artist(artist):
  elt = Artist.query.filter_by(id = artist.id).first()
  if elt:
    db.session.delete(elt)
    db.commit()
    return True
  else:
    return False

def delete_artists():
  Artist.query.delete()
  db.session.commit()
  return True

def add_ifnotexists(session, model, **kwargs):
  obj = model.query.filter_by(**kwargs).first()
  if obj:
    return obj
  else:
      obj = model(**kwargs)
      session.add(obj)
      return obj