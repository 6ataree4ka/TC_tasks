# -*- coding: utf-8 -*-
from .base_page import BasePage
from .base_page import InvalidPageException
from selenium.webdriver.support.ui import Select


class BirthDatePage(BasePage):

    def __init__(self, driver, data_controller, language):
        self.language = language
        super(BirthDatePage, self).__init__(driver, data_controller)

    def _validate_page(self, driver, data_controller):
        try:
            age_validation_element_text = driver.find_element_by_tag_name(
                data_controller.config["site"]["locators"]["tag_name"]).text
            if age_validation_element_text != data_controller.config[
                    "site"]["locators"]["age_validation_text"][self.language]:
                raise Exception()
        except:
            raise InvalidPageException("Enter Birth Date Page not loaded")

    def enter_birth_date(self):
        day = Select(self.driver.find_element_by_xpath(
            self.data_controller.config["site"]["locators"]["age_day"]))
        day.select_by_visible_text("8")

        month = Select(self.driver.find_element_by_xpath(
            self.data_controller.config["site"]["locators"]["age_month"]))
        month.select_by_visible_text("March")

        year = Select(self.driver.find_element_by_xpath(
            self.data_controller.config["site"]["locators"]["age_year"]))
        year.select_by_visible_text("1992")

        self.driver.find_element_by_class_name(self.data_controller.config["site"][
                                               "locators"]["age_submit"]).click()
