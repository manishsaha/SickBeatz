from . import *

@sickbeatz.route('/artists', methods = ['GET'])
def get():
  if 'name' in request.args:
    artists = artists_dao.artists_by_name(request.args['name'])
    data, error = artist_schema.dump(artists, many=True)
    return jsonify(data)
  else:
    artists = artists_dao.get_all_artists()
    data, error = artist_schema.dump(artists, many=True)
    return jsonify(data) 

@sickbeatz.route('/artists', methods = ['POST'])
def post():
    artist = Artist(request.args['name'], request.args['genre'])
    #artist = Artist(**request.args)
    added  = artists_dao.add_artist(artist)
    data, error = artist_schema.dump(added)
    return jsonify({'success': True, 'data': data})

@sickbeatz.route('/artists', methods = ['DELETE'])
def delete():
  if 'name' in request.args:
    artist = artist_schema.get_artist_name(request.args['name'])
    _bool = artists_dao.delete_artist(artist)
    return jsonify({'success': _bool})
  else:
    _bool = artist_schema.delete_artists
    return jsonify({'success': _bool})