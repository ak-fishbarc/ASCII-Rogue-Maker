from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError


def create_forms(db_model):

    forms = Blueprint('forms', __name__)

    class RegisterForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
        email_addr = EmailField('Email', validators=[DataRequired(), Email()])
        submit = SubmitField('Sign up!')

        def validate_username(self, username):
            user = db_model.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError("Please change the username.")
        
        def validate_email(self, email):
            user = db_model.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError("Wrong email address. Please try a different one.")

    class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Login')

    return forms, RegisterForm, LoginForm
