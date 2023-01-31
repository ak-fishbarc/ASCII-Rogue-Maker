from flask import Flask
from flask_bootstrap import Bootstrap
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


def set_up_db_users(db):
    User = initialize_users(db)
    db.relationship(User)
    return User

###############################
# This will need cleaning up. #
###############################


app = create_app()
db = create_db(app)
User = set_up_db_users(db)

db.init_app(app)

forms, RegisterForm = create_forms(User)
app.register_blueprint(forms)
routes = create_routes(RegisterForm)
app.register_blueprint(routes)
app.app_context().push()
db.create_all()

if __name__ == "__main__":
    app.run()


