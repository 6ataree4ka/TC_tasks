# -*- coding: utf-8 -*-
from .base_page import BasePage
from .base_page import InvalidPageException
from selenium.webdriver import ActionChains


class MainPage(BasePage):

    def __init__(self, driver, data_controller):
        super(MainPage, self).__init__(driver, data_controller)

    def _validate_page(self, driver, data_controller):
        url = driver.current_url
        try:
            if url != data_controller.config["site"]["url"]:
                raise Exception()
        except:
            raise InvalidPageException("Main Page not loaded")

    def check_language(self):
        language_checker = self.driver.find_element_by_id(
            self.data_controller.config["site"]["locators"]["language_id"]).text
        if language_checker == "язык":
            return 'ru'
        elif language_checker == "language":
            return 'en'
        else:
            raise Exception("Not supported language")

    def browse_tab(self):
        # Navigate to tab
        tab = self.driver.find_element_by_id(
            self.data_controller.config["site"]["locators"]["tab_id"])
        navigate_to_tab = ActionChains(self.driver)
        navigate_to_tab.move_to_element_with_offset(tab, 5, 5)

    def select_item(self, language):
        # Wait for menu items to appear, then click item
        link_text = self.driver.find_element_by_link_text(
            self.data_controller.config["site"]["locators"]["link_text"][language])
        select_item = ActionChains(self.driver)
        select_item.move_to_element_with_offset(link_text, 5, 5)
        select_item.click()
        select_item.perform()
