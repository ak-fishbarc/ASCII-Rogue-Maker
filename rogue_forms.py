from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


forms = Blueprint('forms', __name__)


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email_addr = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign up!')
