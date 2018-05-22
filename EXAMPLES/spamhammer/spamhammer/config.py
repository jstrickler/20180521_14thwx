#!/usr/bin/env python3
# (c) 2015 John Strickler
#
import os

class BaseConfig(object):
    SECRET_KEY = 'My hovercraft is full of eels'
    SPAMHAMMER_MAIL_PREFIX = '[SpamHammer]'
    SPAMHAMMER_MAIL_SENDER = 'SpamHammer Admin <admin@spamhammer.com>'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    DB_URI = os.environ.get('FLASK_DEV_DATABASE_URL')

class ProductionConfig(BaseConfig):
    DEBUG = False
    DB_URI = os.environ.get('FLASK_PROD_DATABASE_URL')

# not really needed...
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
