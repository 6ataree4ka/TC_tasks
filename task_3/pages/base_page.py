from abc import abstractmethod


class BasePage(object):

    def __init__(self, driver, data_controller):
        self._validate_page(driver, data_controller)
        self.driver = driver
        self.data_controller = data_controller

    @abstractmethod
    def _validate_page(self, driver, data_controller):
        return


class InvalidPageException(Exception):
    # Throw this exception when you don't find the correct page
    pass
