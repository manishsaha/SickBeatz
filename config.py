import os

# Database info

DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']

DATABASE_URL = 'postgresql://{}/{}'.format(DB_HOST, DB_NAME)

basedir = os.path.abspath(os.path.dirname(__file__))

# Different environments for the app to run in

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  CSRF_SESSION_KEY = "secret"
  SECRET_KEY = "not_this"
  SQLALCHEMY_DATABASE_URI = DATABASE_URL
  THREADS_PER_PAGE = 2

class ProductionConfig(Config):
  DEBUG = False

class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
