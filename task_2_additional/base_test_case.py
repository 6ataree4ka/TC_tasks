import os
import unittest
from data_controller import DataController
from browser_factory import BrowserFactory


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        self.data_controller = DataController()
        self.data_controller.read_settings(dir + "\settings.yaml")
        self.login = self.data_controller.config["login"]
        self.password = self.data_controller.config["password"]
        self.output_dir = dir + self.data_controller.config["output_path"]

        browser_factory = BrowserFactory(self.data_controller)
        self.driver = browser_factory.driver

        # Implicit wait 30 seconds
        self.driver.implicitly_wait(30)

        self.driver.maximize_window()
        self.driver.get(self.data_controller.config["url"])

    def tearDown(self):
        self.driver.quit()
