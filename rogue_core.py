from flask import Flask
from flask_bootstrap import Bootstrap
from rogue_routes import routes


app = Flask(__name__)
Bootstrap(app)

app.register_blueprint(routes)


if __name__ == "__main__":
    app.run()
