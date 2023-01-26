from flask import Flask
from flask_bootstrap import Bootstrap
from rogue_routes import routes
from rogue_forms import forms
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import initialize_users


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    app.register_blueprint(routes)
    app.register_blueprint(forms)

    return app


def create_db(app):
    db = SQLAlchemy()
    migrate = Migrate(app, db)

    return db


def set_up_db_users(db):
    User = initialize_users(db)
    # Amazing solution to circular dependency... <3
    db.relationship('User')

    return User


app = create_app()
db = create_db(app)
User = set_up_db_users(db)


if __name__ == "__main__":
    app.run()


