from decouple import config


class Config:
    SECRETE_KEY = config('SECRETE_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}