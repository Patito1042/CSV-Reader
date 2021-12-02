import os

class BaseConfig:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PG_USER = os.environ.get('PG_USER')
    PG_PW = os.environ.get('PG_PW')
    PG_SERVER = os.environ.get('PG_SERVER')
    PG_DB = 'netflix'

class DB_URI:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{BaseConfig.PG_USER}:{BaseConfig.PG_PW}@{BaseConfig.PG_SERVER}/{BaseConfig.PG_DB}'

