import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_BINDS = {
        "game_db": 'sqlite:///' + os.path.join(basedir, 'game.db')
    }
    SECRET_KEY = "just_for_now"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_BINDS = {
        "game_db": 'sqlite:///' + os.path.join(basedir, 'test_game.db')
    }