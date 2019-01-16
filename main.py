# -*- coding: utf-8 -*-
# import time
import unittest

from selenium import webdriver

import configparser
from Pages import main_page
from Pages import flow_page


class UseCaseScenario(unittest.TestCase):
    def setUp(self):

        config = configparser.ConfigParser()
        config.read('config.ini')
        self.driver = webdriver.Chrome(config['ENVIRONMENT']['chromedriver_path'])
        self.wait_timeout = float(config['DEFAULT']['default_wait_timeout'])
        self.driver.set_page_load_timeout(config['DEFAULT']['page_load_timeout'])
        self.driver.implicitly_wait(self.wait_timeout)
        self.verificationErrors = []
        self.accept_next_alert = True

        self.main_page = main_page.MainPage(self.driver, self.wait_timeout)
        self.commit_page = flow_page.CommitPage(self.driver, self.wait_timeout)

    def test_scenario(self):
        cp = self.commit_page
        flow_page_sha = cp.get_latest_commit_id()
        mp = self.main_page
        main_page_sha = mp.get_latest_commit_id()

        assert flow_page_sha == main_page_sha, "SHA on the main page != SHA of latest commit on commit page"

    def tearDown(self):
        self.main_page.destroy()
        self.commit_page.destroy()

        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
