import unittest

from werkzeug.test import Client
from rogue_core import app


class TestBack(unittest.TestCase):

    def setUp(self):
        self.server = Client(app)

    def test_back_of_home(self):
        response = self.server.get('/')
        ids = ["sign-up", "log-in", "game-edit"]
        self.assertEqual(response.status_code, 200)
        for i in ids:
            self.assertIn(i, response.data.decode())


if __name__ == '__main__':
    unittest.main()
