from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
import time

from rogue_core import db, game_db, User, Game


class TestFirst(unittest.TestCase):
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
        4. Game Editor
        """
        ids = ["Sign-Up", "Login"]
        for i in ids:
            self.browser.get('http://localhost:5000')
            self.browser.find_element(By.LINK_TEXT, i).click()

    # Open http://localhost:5000/signup to find a registration form.
    def test_01_front_of_signup(self):
        self.browser.get('http://localhost:5000/signup')
        form = self.browser.find_element(By.TAG_NAME, 'form')

        # Find input fields.
        ids = ["username", "password", "password2", "email_addr", "submit"]
        these_keys = ["Jon Irenicus", "operationAurora", "operationAurora", "jon.irenicus@imaginary.co.uk"]

        # Create an account.
        i = 0
        while i < len(these_keys):
            time.sleep(1)
            field = self.browser.find_element(By.ID, ids[i])
            field.send_keys(these_keys[i])
            i += 1
        form.submit()

        time.sleep(1)
        check_page = self.browser.current_url
        self.assertNotEqual(check_page, 'http://localhost:5000/signup')

    # Open http://localhost:5000/login to find a login form.
    def test_02_front_of_login(self):
        self.browser.get('http://localhost:5000/login')
        form = self.browser.find_element(By.TAG_NAME, 'form')
        # Find input fields.
        ids = ["username", "password", "submit"]
        these_keys = ["Jon Irenicus", "operationAurora"]
        # Login to account.
        i = 0
        while i < len(these_keys):
            time.sleep(1)
            field = self.browser.find_element(By.ID, ids[i])
            field.send_keys(these_keys[i])
            i += 1
        form.submit()

        time.sleep(1)
        check_page = self.browser.current_url
        self.assertNotEqual(check_page, 'http://localhost:5000/login')

        self.browser.get('http://localhost:5000/user/Jon Irenicus')
        check_title = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertNotEqual(check_title.text, "Unauthorized")

        time.sleep(1)
        self.browser.get('http://localhost:5000/home')
        self.browser.find_element(By.LINK_TEXT, "Logout")
        self.browser.find_element(By.LINK_TEXT, "Game Editor").click()
        check_page = self.browser.current_url
        self.assertNotEqual(check_page, 'http://localhost:5000/home')

    def test_03_front_of_game_editor(self):
        self.browser.get('http://localhost:5000/login')
        form = self.browser.find_element(By.TAG_NAME, 'form')
        # Find input fields.
        ids = ["username", "password", "submit"]
        these_keys = ["Jon Irenicus", "operationAurora"]
        # Login to account.
        i = 0
        while i < len(these_keys):
            time.sleep(1)
            field = self.browser.find_element(By.ID, ids[i])
            field.send_keys(these_keys[i])
            i += 1
        form.submit()

        time.sleep(1)
        self.browser.get('http://localhost:5000/game_editor')
        form = self.browser.find_element(By.TAG_NAME, 'form')
        ids = ["gamename"]
        these_keys = ["Test Game"]
        i = 0
        while i < len(these_keys):
            time.sleep(1)
            field = self.browser.find_element(By.ID, ids[i])
            field.send_keys(these_keys[i])
            i += 1
        form.submit()

        self.browser.get('http://localhost:5000/game/Test Game')
        check_title = self.browser.find_element(By.TAG_NAME, 'title')
        self.assertNotIn("404", check_title.text)
        check_title = self.browser.find_element(By.TAG_NAME, 'title')
        self.assertNotIn("Unauthorized", check_title.text)

    def test_04_drop_database_changes(self):
        clean_up = User.query.filter_by(username="Jon Irenicus").first()
        db.session.delete(clean_up)
        db.session.commit()

        clean_up = Game.query.filter_by(gamename="Test Game").first()
        game_db.session.delete(clean_up)
        game_db.session.commit()


if __name__ == "__main__":
    unittest.main()
