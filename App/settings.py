import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def db_to_uri(db_info):
    engine = db_info.get("ENGINE") or "sqlite"
    driver = db_info.get("DRIVER") or "sqlite"
    user = db_info.get("USER") or ""
    password = db_info.get("PASSWORD") or ""
    host = db_info.get("HOST") or ""
    port = db_info.get("PORT") or ""
    name = db_info.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    TESTING = False
    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'
    CACHE_TYPE = 'redis'
    SECRET_KEY = "456748787adsdas45das4d57df5sd"

    # MAIL_SERVER = 'localhost'
    # MAIL_PORT = 25
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = False
    # MAIL_DEBUG = app.debug
    # MAIL_USERNAME = None
    # MAIL_PASSWORD = None
    # MAIL_DEFAULT_SENDER = 'WQK'
    # MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = app.testing
    # MAIL_ASCII_ATTACHMENTS = False


class DevelopConfig(Config):
    DEBUG = True

    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "FlaskSecure",
    }

    SQLALCHEMY_DATABASE_URI = db_to_uri(db_info)

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'abc69317780'
    MAIL_PASSWORD = 'WFENGENGEAEAQXAP'
    MAIL_DEFAULT_SENDER = 'Flask Weekly <%s>' % "abc69317780@163.com"


class TestConfig(Config):
    TESTING = True

    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "FlaskSecure",
    }

    SQLALCHEMY_DATABASE_URI = db_to_uri(db_info)


class StagingConfig(Config):

    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "FlaskSecure",
    }

    SQLALCHEMY_DATABASE_URI = db_to_uri(db_info)


class ProductConfig(Config):

    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "FlaskSecure",
    }

    SQLALCHEMY_DATABASE_URI = db_to_uri(db_info)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig,
}