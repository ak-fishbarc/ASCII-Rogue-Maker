import unittest

from werkzeug.test import Client
from rogue_core import app


class TestBack(unittest.TestCase):

    def setUp(self):
        self.server = Client(app)

    def test_back_of_home(self):
        response = self.server.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
