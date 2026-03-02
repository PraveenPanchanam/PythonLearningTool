import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-do-not-use-in-production')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600  # 1 hour

    # Sandbox settings
    SANDBOX_MODE = os.environ.get('SANDBOX_MODE', 'subprocess')  # 'subprocess' or 'docker'
    SANDBOX_IMAGE = os.environ.get('SANDBOX_IMAGE', 'pythonlearning-sandbox:latest')
    SANDBOX_TIMEOUT = int(os.environ.get('SANDBOX_TIMEOUT', '10'))
    SANDBOX_MEMORY_LIMIT = os.environ.get('SANDBOX_MEMORY_LIMIT', '256m')

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'pythonlearning.db')


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Must be set in production

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # Fix Heroku/Render postgres:// -> postgresql:// issue
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql+psycopg://', 1)

    # Use psycopg3 driver (postgresql:// -> postgresql+psycopg://)
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgresql://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgresql://', 'postgresql+psycopg://', 1)

    # Secure cookies (only enforce Secure flag when behind HTTPS / reverse proxy)
    _use_https = os.environ.get('FORCE_HTTPS', 'false').lower() == 'true'
    SESSION_COOKIE_SECURE = _use_https
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_SECURE = _use_https
    REMEMBER_COOKIE_HTTPONLY = True

    # Rate limiting
    RATELIMIT_STORAGE_URI = os.environ.get('REDIS_URL', 'memory://')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
