import unittest
from util.data_controller import DataController
from util.browser_factory import BrowserFactory


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.config = DataController.instance().config

        self.driver = BrowserFactory.instance().driver

        self.driver.implicitly_wait(self.config["wait"])
        self.driver.maximize_window()
        self.driver.get(self.config["site"]["url"])

    def tearDown(self):
        self.driver.quit()
