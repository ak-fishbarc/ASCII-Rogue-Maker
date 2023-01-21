from flask import Flask
from flask_bootstrap import Bootstrap
from rogue_routes import routes
from rogue_forms import forms
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
db = SQLAlchemy(app)
# Amazing solution to circular dependency... <3
db.relationship('User')
migrate = Migrate(app, db)

app.register_blueprint(routes)
app.register_blueprint(forms)


if __name__ == "__main__":
    app.run()


