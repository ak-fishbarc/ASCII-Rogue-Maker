from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin
from rogue_routes import create_routes
from rogue_forms import create_forms
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import initialize_users


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


# Create app.
app = create_app()
login = LoginManager(app)

# Set up database.
db = create_db(app)
User = set_up_db_users(db, UserMixin, login)
db.init_app(app)

# Set up blueprints.
forms, RegisterForm, LoginForm = create_forms(User)
app.register_blueprint(forms)
routes = create_routes(RegisterForm, LoginForm, User, db)
app.register_blueprint(routes)

# Build everything up.
app.app_context().push()
db.create_all()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


if __name__ == "__main__":
    app.run()


