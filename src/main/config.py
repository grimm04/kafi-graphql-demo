"""Flask configuration."""
import os
from datetime import timedelta
from os import environ, path
from dotenv import load_dotenv

basedir = os.getcwd()
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'  
    PREFIX = 'wskf_'
    CORS_ORIGINS = "http://127.0.0.1:5000"
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_POOL_TIMEOUT = 20


    # DB
    # DRIVERNAME=environ.get('DRIVERNAME'),
    # USERNAME=environ.get('USERNAME'),
    # PASSWORD=environ.get('PASSWORD'),
    # HOST=environ.get('HOST'),
    # PORT=environ.get('PORT'),
    # DATABASE=environ.get('DATABASE'),
    # QUERY=environ.get('QUERY')

    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')
    BCRYPT_LOG_ROUNDS = 12
    JWT_ACCESS_TOKEN_EXPIRES  =  timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

class ProdConfig(Config): 
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config): 
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    

config_by_name = dict(
    dev=DevConfig,
    test=TestingConfig,
    prod=ProdConfig
)

key = Config.SECRET_KEY