from abc import abstractmethod

import sys
import os
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "util"))
sys.path.append(file_path)
from util.browser_factory import BrowserFactory
from util.data_controller import DataController


class BasePage(object):

    def __init__(self, **kwargs):
        driver = BrowserFactory.instance().driver
        config = DataController.instance().config
        self._validate_page(driver, config, **kwargs)
        self.driver = driver
        self.config = config

    @abstractmethod
    def _validate_page(self, driver, config, **kwargs):
        return


class InvalidPageException(Exception):
    # Throw this exception when you don't find the correct page
    pass
