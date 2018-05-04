from . import *

@sickbeatz.route('/likes', methods = ['GET'])
def get():
  if 'a_name' in request.args:
    artist = artist_dao.get_artist_name(request.args['a_name'])
    likers = likes_dao.all_likers(artist)
    data, error = user_schema.dump(likers, many=True)
    return jsonify(data)
  else:
    user = user_dao.get_user_name(request.args['u_name'])
    likings = likes.dao.all_likings(user)
    data, error = artist_schema.dump(likings, many=True)
    return jsonify(data)

@sickbeatz.route('/likes', methods = ['POST'])
def post():
  usr = users_dao.get_user_name(request.args['user_name'])
  artist_name = request.args['artist_name']
  artist_genre = request.args['artist_genre']
  art = artists_dao.add_ifnotexists(db.session, Artist, name = artist_name,\
    genre = artist_genre)
  like = likes_dao.add_like(usr,art)    
  data, error = like_schema.dump(like)
  return jsonify(data)

@sickbeatz.route('/likes', methods = ['DELETE'])
def delete():
  if 'name' in request.args:
    usr = users.dao.get_user_name(request.args['name'])
    _bool = likes_dao.delete_all_likes()
    return jsonify({'success': _bool})
  else:
    usr = users_dao.get_user_id(request.args['user_id'])
    art = artists_dao.get_artist_id(request.args['artist_id'])
    _bool = likes_dao.delete_like(usr,art)    
    return jsonify({'success': _bool})