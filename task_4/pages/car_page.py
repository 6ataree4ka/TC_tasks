from .base_page import BasePage
from .base_page import InvalidPageException

import sys
import os
base_path = os.path.dirname(__file__)
elements_file_path = os.path.abspath(os.path.join(base_path, "..", "elements"))
util_file_path = os.path.abspath(os.path.join(base_path, "..", "util"))
sys.path.append(elements_file_path)
sys.path.append(util_file_path)
from elements.tab_element import Tab
from util.locators import CarPageLocators


class CarPage(BasePage):

    def __init__(self, **kwargs):
        super(CarPage, self).__init__(**kwargs)

    def _validate_page(self, driver, config, **kwargs):
        url = driver.current_url
        # Use http/https replaces to normalize site links (because some of them httpS, other http)
        url = url.replace('https://', '').replace('http://', '')
        target_url = (config["site"]["url"] + kwargs.get("car_brand").lower().replace(' ', '-') +
                      "/" + kwargs.get("car_model").lower().replace(' ', '-') +
                      "/" + kwargs.get("car_year") + "/consumer-reviews/").replace('https://', '').replace('http://', '')
        try:
            if url != target_url:
                raise Exception()
        except:
            raise InvalidPageException("Car Page not loaded")

    def switch_to_tab(self):
        overview_tab = Tab(CarPageLocators.OVERVIEW_TAB)
        overview_tab.click()
