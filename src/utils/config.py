class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    USERNAME = ''
    PASSWORD = ''

class ProductionConfig(Config):
    USERNAME = ''
    PASSWORD = ''
    DATABASE_URI = ''

class TestingConfig(Config):
    TESTING = True
    USERNAME = ''
    PASSWORD = ''
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_NAME = ''
    DB_IP = ''
    DB_PORT = 0
    DATABASE_URI = 'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_IP}:{DB_PORT}/{DB_NAME}'.format(**locals())

def get_config(env):
    env_dict = {
        'dev': DevelopmentConfig,
        'test': TestingConfig,
        'production': ProductionConfig
    }
    return env_dict[env]