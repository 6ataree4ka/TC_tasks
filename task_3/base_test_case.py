import os
import unittest
from util.data_controller import DataController
from util.browser_factory import BrowserFactory
import shutil


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        self.data_controller = DataController()
        self.data_controller.read_settings(dir + "\settings.yaml")
        # Create downloads folder if it does not exist
        if not os.path.exists(dir + self.data_controller.config["downloads_dir"]):
            os.makedirs(dir + self.data_controller.config["downloads_dir"])

        browser_factory = BrowserFactory(self.data_controller, dir)
        self.driver = browser_factory.driver
        self.driver.implicitly_wait(self.data_controller.config["wait"])

        self.driver.maximize_window()
        self.driver.get(self.data_controller.config["site"]["url"])
        self.driver.implicitly_wait(self.data_controller.config["wait"])

    def tearDown(self):
        dir = os.path.dirname(__file__)
        # Do not open downloads folder during the test, because it leads to error
        # Delete downloads folder with content after test finished
        shutil.rmtree(dir + self.data_controller.config["downloads_dir"])
        self.driver.quit()
