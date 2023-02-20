from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin
from rogue_routes import create_routes
from rogue_forms import create_forms, create_game_forms
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import initialize_users, initialize_game


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    return app


def create_db(app):
    db = SQLAlchemy()
    migrate = Migrate(app, db)
    return db


def set_up_db_users(db, UserMixin, login):
    User = initialize_users(db, UserMixin, login)
    db.relationship(User)
    return User


def set_up_db_game(db):
    Game = initialize_game(db)
    db.relationship(Game)
    return Game


# Create app.
app = create_app()
login = LoginManager(app)

# Set up database.
db = create_db(app)
User = set_up_db_users(db, UserMixin, login)
db.init_app(app)

# Set up second database for game related data. As there will be more user
# interaction in game editing, so user database and game database are separate.
game_db = create_db(app)
Game = set_up_db_game(game_db)
game_db.init_app(app)

# Set up blueprints.
forms, RegisterForm, LoginForm = create_forms(User)
game_forms, NewGameForm = create_game_forms(Game)

app.register_blueprint(game_forms)
app.register_blueprint(forms)
routes = create_routes(RegisterForm, LoginForm, NewGameForm, User, Game, db)
app.register_blueprint(routes)

# Build everything up.
app.app_context().push()
db.create_all()
game_db.create_all()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


if __name__ == "__main__":
    app.run()


