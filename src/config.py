from decouple import config


class Config:
    SECRETE_KEY = config('SECRETE_KEY')


class DevelopmentConfig(Config):
    DEBUG = True

Config={
    'development': DevelopmentConfig
}