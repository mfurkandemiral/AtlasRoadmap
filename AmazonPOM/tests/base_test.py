import unittest
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BaseTest  (unittest.TestCase):
    base_url = "https://www.amazon.com"

    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(15)
        self.logger = logging.getLogger()

    def tearDown(self):
        self.driver.close()