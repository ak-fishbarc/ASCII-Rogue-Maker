import unittest

from werkzeug.test import Client
from rogue_core import create_app, create_db, set_up_db_users, UserMixin
from rogue_forms import create_forms
from rogue_routes import create_routes
from config import TestingConfig


class TestBack(unittest.TestCase):

    def setUp(self):

        # Create app.
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.server = Client(self.app)

        # Create database.
        self.db = create_db(self.app)
        self.User = set_up_db_users(self.db, UserMixin)
        self.db.init_app(self.app)

        # Set up routes.
        forms, RegisterForm, LoginForm = create_forms(self.User)
        self.app.register_blueprint(forms)
        routes = create_routes(RegisterForm, LoginForm, self.User, self.db)
        self.app.register_blueprint(routes)

        # Build up.
        self.app.app_context().push()
        self.db.create_all()

    def tearDown(self):
        self.db.drop_all()

    def test_back_of_home(self):
        response = self.server.get('/')
        ids = ['<a href="/signup">', "log-in", "game-edit"]
        self.assertEqual(response.status_code, 200)
        for i in ids:
            self.assertIn(i, response.data.decode())

    def test_back_of_signup(self):
        response = self.server.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.data.decode())

    def test_back_of_login(self):
        response = self.server.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.data.decode())

    def test_db_user_model(self):
        u = self.User(username="DecardCain", email="DecardCain@example.co.uk")
        self.db.session.add(u)
        self.db.session.commit()

        query_users = self.User.query.all()
        self.assertIn("DecardCain", query_users[0].username)


if __name__ == '__main__':
    unittest.main()

