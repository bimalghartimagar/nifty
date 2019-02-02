import os

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_NAME = ''
    DB_IP = ''
    DATABASE_URL = 'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_IP}'.format(**locals())
    # For heroku
    DATABASE_URL = os.getenv('DATABASE_URL', DATABASE_URL) 

class TestingConfig(Config):
    TESTING = True
    
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_NAME = ''
    DB_IP = ''
    DATABASE_URL = 'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_IP}'.format(**locals())

class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_NAME = ''
    DB_IP = ''
    DB_PORT = 0
    DATABASE_URL = 'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_IP}:{DB_PORT}/{DB_NAME}'.format(**locals())

def get_config():
    
    env_type = os.environ.get('ENV_TYPE', 'dev')
    
    env_dict = {
        'dev': DevelopmentConfig,
        'test': TestingConfig,
        'production': ProductionConfig
    }
    
    return env_dict[env_type]
