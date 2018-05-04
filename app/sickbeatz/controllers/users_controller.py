from . import *

@sickbeatz.route('/users', methods = ['GET'])
def uget():
  if 'name' in request.args:
    usr = user_dao.get_user_name(request.args['name'])
    data, error = user_schema.dump(usr)
    return jsonify(data)
  else:
    usrs = user_dao.get_users()
    data, error = user_schema.dump(usrs, many=True)
    return jsonify(data)

@sickbeatz.route('/users', methods = ['POST'])
def upost():
  usr = User(name = request.args['name'], email = request.args['email'],\
    age = request.args['age'])
  #usr = User(**request)
  data, error = user_schema.dump(users_dao.add_user(usr))
  return jsonify(data)

@sickbeatz.route('/users', methods = ['DELETE'])
def udelete():
  if 'name' in request.args:
    usr = user_dao.get_user_name(request.args['name'])
    _bool = user_dao.delete_user(usr)
    return jsonify({'success' : _bool})
  else:
    _bool = user_dao.delete_users()
    return jsonify({'success' : _bool})