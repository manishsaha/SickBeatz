from . import *

@sickbeatz.route('/likes', methods = ['GET'])
def lget():
  if 'aid' in request.args:
    artist = artists_dao.get_artist_id(request.args['aid'])
    likers = likes_dao.all_likers(artist)
    data, error = user_schema.dump(likers, many=True)
    return jsonify(data)
  else:
    user = users_dao.get_user_id(request.args['uid'])
    likings = likes_dao.all_likings(user)
    data, error = artist_schema.dump(likings, many=True)
    return jsonify(data)

@sickbeatz.route('/likes', methods = ['POST'])
def lpost():
  usr = users_dao.get_user_name(request.args['user_name'])
  artist_name = request.args['artist_name']
  artist_genre = request.args['artist_genre']
  art = artists_dao.add_ifnotexists(db.session, Artist, name = artist_name,\
    genre = artist_genre)
  like = likes_dao.add_like(art,usr)
  if like:    
    data, error = like_schema.dump(like)
    adata, err1 = artist_schema.dump(artists_dao.get_artist_id(like.artist_id))
    udata, err2 = user_schema.dump(users_dao.get_user_id(like.user_id))
    return jsonify({'success': True, 'like': \
      data, 'artist': adata, 'user': udata})
  else: return jsonify ({'success': False})

@sickbeatz.route('/likes', methods = ['DELETE'])
def ldelete():
  if 'id' in request.args:
    usr = users_dao.get_user_id(request.args['id'])
    _bool = likes_dao.delete_likes(usr)
    return jsonify({'success': _bool})
  else:
    usr = users_dao.get_user_id(request.args['uid'])
    art = artists_dao.get_artist_id(request.args['aid'])
    _bool = likes_dao.delete_like(art,usr)    
    return jsonify({'success': _bool})