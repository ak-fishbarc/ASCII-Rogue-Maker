from flask import Blueprint
from flask import render_template, redirect, url_for


def create_routes(RegisterForm, User, db):

    routes = Blueprint('routes', __name__)

    @routes.route("/")
    @routes.route("/home")
    def home():
        return render_template('home.html')

    @routes.route("/signup", methods=["GET", "POST"])
    def signup():
        form = RegisterForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email_addr.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('routes.home'))
        return render_template('signup.html', form=form)

    return routes
