from flask import request, render_template, jsonify
from functools import wraps # for decorators
import app

# Models
from app.sickbeatz.models.all import *

# DAO
from app.sickbeatz.dao import artists_dao, \
  users_dao, \
  likes_dao, \
  songs_dao

# Serializers
artist_schema         = ArtistSchema()
like_schema           = LikeSchema()
song_schema           = SongSchema()
user_schema           = UserSchema()

# Blueprint
from app.sickbeatz import sickbeatz
