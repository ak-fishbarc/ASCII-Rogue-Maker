from flask import Blueprint
from flask import render_template
from rogue_forms import RegisterForm


routes = Blueprint('routes', __name__)


@routes.route("/")
def home():
    return render_template('home.html')


@routes.route("/signup")
def signup():
    form = RegisterForm()
    return render_template('signup.html', form=form)
