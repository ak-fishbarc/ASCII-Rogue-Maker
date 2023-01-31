import unittest

from werkzeug.test import Client
from rogue_core import create_app, create_db, set_up_db_users
from rogue_forms import create_forms
from rogue_routes import create_routes
from config import TestingConfig


class TestBack(unittest.TestCase):

    def setUp(self):
        ########################
        # Clean this up next.  #
        ########################
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.db = create_db(self.app)
        self.db.init_app(self.app)
        self.server = Client(self.app)
        self.User = set_up_db_users(self.db)
        forms, RegisterForm = create_forms(self.User)
        self.app.register_blueprint(forms)
        routes = create_routes(RegisterForm)
        self.app.register_blueprint(routes)
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

    def test_db_user_model(self):
        u = self.User(username="DecardCain", email="DecardCain@example.co.uk")
        self.db.session.add(u)
        self.db.session.commit()

        query_users = self.User.query.all()
        self.assertIn("DecardCain", query_users[0].username)


if __name__ == '__main__':
    unittest.main()

