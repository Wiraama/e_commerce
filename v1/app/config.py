import os

class Config:
    "base Configuration"
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///e_commerce.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLACHEMY_DATABASE_URI = 'sqlite:///:memory:'

config_by_name = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}