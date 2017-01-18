import os
from selenium import webdriver
from .singleton import Singleton
from .data_controller import DataController


@Singleton
class BrowserFactory(object):

    def __init__(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, ".."))

        browser = DataController.instance().config["browser"]

        # Select browser (chrome/firefox/ie are possible values)
        if browser == "chrome":
            chrome_driver_path = file_path + \
                DataController.instance().config["drivers"]["chrome"]
            self.driver = webdriver.Chrome(chrome_driver_path)
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            ie_driver_path = file_path + \
                DataController.instance().config["drivers"]["ie"]
            self.driver = webdriver.Ie(ie_driver_path)
        else:
            self.driver = webdriver.Firefox()
