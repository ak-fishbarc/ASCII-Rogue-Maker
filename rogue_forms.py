from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, RadioField
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


def create_game_forms(db_model):

    game_forms = Blueprint('game_forms', __name__)

    class NewGameForm(FlaskForm):
        gamename = StringField('Gamename', validators=[DataRequired()])
        submit = SubmitField('Create New Game')

        def validate_gamename(self, gamename):
            new_game = db_model.query.filter_by(gamename=gamename.data).first()
            if new_game is not None:
                raise ValidationError("Please change the name.")

    class NewTileForm(FlaskForm):
        tilename = StringField('Tilename', validators=[DataRequired()])
        tileicons = RadioField('Tileicons', choices=[' . ', '  ', ' , '], validators=[DataRequired()])
        submit = SubmitField('Create Tile')

    return game_forms, NewGameForm, NewTileForm
