import unittest

from werkzeug.test import Client
from rogue_core import app, db
from models import User


class TestBack(unittest.TestCase):

    def setUp(self):
        app.app_context().push()
        self.server = Client(app)
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_back_of_home(self):
        response = self.server.get('/')
        ids = ["sign-up", "log-in", "game-edit"]
        self.assertEqual(response.status_code, 200)
        for i in ids:
            self.assertIn(i, response.data.decode())

    def test_back_of_signup(self):
        response = self.server.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.data.decode())

    def test_db_user_model(self):
        u = User(username="DecardCain", email="DecardCain@example.co.uk")
        db.session.add(u)
        db.session.commit()

        query_users = User.query.all()
        self.assertIn("DecardCain", query_users[0].username)


if __name__ == '__main__':
    unittest.main()

