from . import *

@sickbeatz.route('/users', methods = ['GET', 'POST', 'DELETE'])
  else:
        usr = artists_dao.add_user(User(request))
      return jsonify(user_schema.dump(usr))