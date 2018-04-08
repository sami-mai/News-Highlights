import os

class Config:
    '''
    General configuartion parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&country={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
            config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
