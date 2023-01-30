from flask import Blueprint
from flask import render_template, redirect
from rogue_forms import RegisterForm


routes = Blueprint('routes', __name__)


@routes.route("/")
def home():
    return render_template('home.html')


@routes.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('signup.html', form=form)
