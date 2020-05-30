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
    SECRET_KEY = "456748787adsdas45das4d57df5sd"


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