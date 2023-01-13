

class Config(object):
    SECRET_KEY = 'secret_key'
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    database: str = 'db'
    collection: str = 'files'
    MONGODB_URI = 'mongodb://root:1234@db:27017'
    

dev_settings = DevelopmentConfig()
