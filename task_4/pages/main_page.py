# -*- coding: utf-8 -*-
from .base_page import BasePage
from .base_page import InvalidPageException

import sys
import os
base_path = os.path.dirname(__file__)
elements_file_path = os.path.abspath(os.path.join(base_path, "..", "elements"))
util_file_path = os.path.abspath(os.path.join(base_path, "..", "util"))
sys.path.append(elements_file_path)
sys.path.append(util_file_path)
from elements.button_element import Button
from elements.menu_item_element import MenuItem
from util.locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

    def _validate_page(self, driver, config, **kwargs):
        url = driver.current_url
        # To normalize site links (because some of them httpS, other http)
        url = url.replace('https://', '').replace('http://', '')
        target_url = config["site"]["url"].replace(
            'https://', '').replace('http://', '')
        try:
            if url != target_url:
                driver.get(config["site"]["url"])
        except:
            raise InvalidPageException("Main Page not loaded")

    def open_menu(self):
        buy_button = Button(MainPageLocators.BUY_BUTTON)
        buy_button.click()

    def select_menu_item(self):
        menu_item = MenuItem(MainPageLocators.REVIEW_CAR_MENU_ITEM)
        menu_item.click()
