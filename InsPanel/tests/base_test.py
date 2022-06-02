import logging
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = "https://seleniumautomation.inone.useinsider.com/"

    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        option.add_argument('--allow-running-insecure-content')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(15)
        self.logger = logging.getLogger()

    def tearDown(self):
        self.driver.close()