import os
# from instance.config import NEWS_API_KEY

class Config:
    '''General configuration parent class'''

    NEWS_API_BASE_URL =  'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLES_API_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}' 

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''Production configuration child class
    Args:
        Config: The parent configuration  class with general configuration settings'''

    pass

class DevConfig(Config):
    '''Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings'''

    DEBUG=True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


