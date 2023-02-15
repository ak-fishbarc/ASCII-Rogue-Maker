from flask import Blueprint, flash
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user


def create_routes(RegisterForm, LoginForm, User, db):

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

    @routes.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('routes.home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash("Invalid username or password")
                return redirect(url_for('routes.login'))
            login_user(user)
            return redirect(url_for('routes.home'))
        return render_template('login.html', form=form)

    @routes.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for('routes.home'))

    return routes
