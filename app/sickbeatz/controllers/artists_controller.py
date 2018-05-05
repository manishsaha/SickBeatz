from . import *

@sickbeatz.route('/artists', methods = ['GET'])
def aget():
  if 'name' in request.args:
    artists = artists_dao.artists_by_name(request.args['name'])
    data, error = artist_schema.dump(artists, many=True)
    return jsonify(data)
  else:
    artists = artists_dao.get_all_artists()
    data, error = artist_schema.dump(artists, many=True)
    return jsonify(data)

@sickbeatz.route('/artists', methods = ['POST'])
def apost():
    name = request.args['name']
    genre = request.args['genre']
    artist = Artist(name = name, genre = genre)
    added  = artists_dao.add_artist(artist)
    data, error = artist_schema.dump(added)
    return jsonify({'success': True, 'data': data})

@sickbeatz.route('/artists', methods = ['DELETE'])
def adelete():
  if 'name' in request.args:
    artist = artists_dao.get_artist_name(request.args['name'])
    _bool = artists_dao.delete_artist(artist)
    if _bool:
      data, error = artist_schema.dump(artist)
      return jsonify({'success': _bool, 'data': data})
    else:
      return jsonify({'success': _bool})
  else:
    _bool = artists_dao.delete_artists()
    return jsonify({'success': _bool})