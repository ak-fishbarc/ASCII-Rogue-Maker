from flask import Blueprint
# from flask import render_template


routes = Blueprint('routes', __name__)


@routes.route("/")
def home():
    return "<title> ASCII Rogue</title>"


