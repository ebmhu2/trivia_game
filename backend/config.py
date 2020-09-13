# config.py
"""Flask configuration file"""
from os import environ, path
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))
# load environment variables file
load_dotenv(path.join(basedir, '.env'))

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    SECRET_KEY = environ.get('SECRET_KEY','Hack_Me')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')


class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI_TEST')


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

