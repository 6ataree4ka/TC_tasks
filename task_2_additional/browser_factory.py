import os
from selenium import webdriver


class BrowserFactory(object):

    def __init__(self, data_controller):
        dir = os.path.dirname(__file__)
        browser = data_controller.config["browser"]
        # Select browser (chrome/firefox/ie are possible values)
        if browser == "chrome":
            chrome_driver_path = dir + \
                data_controller.config["drivers"]["chrome"]
            self.driver = webdriver.Chrome(chrome_driver_path)
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            ie_driver_path = dir + data_controller.config["drivers"]["ie"]
            self.driver = webdriver.Ie(ie_driver_path)
        else:
            self.driver = webdriver.Firefox()
