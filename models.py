from werkzeug.security import generate_password_hash, check_password_hash


def initialize_users(db, UserMixin, login):

    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True)
        email = db.Column(db.String(120), index=True, unique=True)
        password_enc = db.Column(db.String(128))

        def set_password(self, password):
            self.password_enc = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_enc, password)

        def __repr__(self):
            return 'User {}?'.format(self.username)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return User


def initialize_game(db):

    class Game(db.Model):
        __bind_key__ = "game_db"
        id = db.Column(db.Integer, primary_key=True)
        gamename = db.Column(db.String(64), index=True, unique=True)
        user_id = db.Column(db.Integer, index=True, unique=True)

    class Tiles(db.Model):
        __bind_key__ = "game_db"
        id = db.Column(db.Integer, primary_key=True)
        tilename = db.Column(db.String(64), index=True, unique=True)
        tileicon = db.Column(db.String(5), index=True, unique=False)
        game_id = db.Column(db.Integer, index=True, unique=True)
    return Game, Tiles


