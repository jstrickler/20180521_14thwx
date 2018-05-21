#!/usr/bin/env python3
# (c) 2015 John Strickler
#
import os

class Config(object):
    SECRET_KEY = 'My hovercraft is full of eels'
    SPAMHAMMER_MAIL_PREFIX = '[KnightsThree]'
    SPAMHAMMER_MAIL_SENDER = 'KnightsThree Admin <admin@KnightsThree.com>'

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:scripts@localhost/postgres'

class ProdConfig(Config):
    DB_URI = os.environ.get('DATABASE_URL')

# not really needed...
config = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': DevConfig
}
