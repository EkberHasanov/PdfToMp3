

from typing import Set


class Config(object):
    SECRET_KEY = 'secret_key'
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    database: str = 'db'
    pdf_collection: str = 'pdf'
    mp3_collection: str = 'mp3'
    MONGODB_URI = 'mongodb://root:1234@db:27017'
    broker_host: str = 'rabbitmq'
    broker_port: int = 5672
    BROKER_URI = 'amqp://admin:1234@rabbitmq:5672'
    ALLOWED_EXTENSIONS: Set[str] = {'pdf'}


dev_settings = DevelopmentConfig()
