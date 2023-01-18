from flask import Flask
from flask_bootstrap import Bootstrap

from rogue_routes import routes
from rogue_forms import forms


app = Flask(__name__)
app.config['SECRET_KEY'] = "just_for_now"
Bootstrap(app)

app.register_blueprint(routes)
app.register_blueprint(forms)


if __name__ == "__main__":
    app.run()
