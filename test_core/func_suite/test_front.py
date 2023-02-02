from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
import time


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
        ids = ["Sign-Up"]
        for i in ids:
            self.browser.find_element(By.LINK_TEXT, i).click()

    # Open http://localhost:5000/signup to find a registration form.
    def test_front_of_signup(self):
        self.browser.get('http://localhost:5000/signup')
        form = self.browser.find_element(By.TAG_NAME, 'form')

        # Find input fields.
        ids = ["username", "password", "password2", "email_addr", "submit"]
        these_keys = ["Jon Irenicus", "operationAurora", "operationAurora", "jon.irenicus@imaginary.co.uk"]

        # Create an account.
        i = 0
        while i < len(these_keys):
            time.sleep(3)
            field = self.browser.find_element(By.ID, ids[i])
            field.send_keys(these_keys[i])
            i += 1
        form.submit()

        time.sleep(3)
        check_page = self.browser.current_url
        self.assertNotEqual(check_page, 'http://localhost:5000/signup')


if __name__ == "__main__":
    unittest.main()
