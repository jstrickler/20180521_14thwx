#!/usr/bin/env python3
# (c) 2015 John Strickler
#
import threading
import unittest
import time

from presidents_template import app

t = threading.Thread(target=app.run)
t.start()
time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPresidents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('localhost:5000')

    def tearDown(self):
        self.driver.close()

    def test_main_screen_has_president_text(self):
        self.assertIn('president', self.driver.page_source, "Page source does not contain 'president")


if __name__ == '__main__':
    unittest.main()

