import os


class BaseConfig(object):
    """Standard configuration options"""
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 2
    SECRET_KEY = "secret"


class TestConfig(BaseConfig):
    """Configuration for unit testing"""
    TESTING = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
    WTF_CSRF_ENABLED = False