from selenium import webdriver
# from selenium.webdriver.common.by import By

import unittest


class TestFront(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # Open browser to find home page
    def test_front_of_home(self):
        self.browser.get('http://localhost:5000')

    """
    Look at the menu. See available options: 
    1. Sign-Up
    2. Log-In
    3. Game Editor
    """


if __name__ == "__main__":
    unittest.main()
