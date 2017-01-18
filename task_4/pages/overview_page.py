from .base_page import BasePage
from .base_page import InvalidPageException

import sys
import os
base_path = os.path.dirname(__file__)
elements_file_path = os.path.abspath(os.path.join(base_path, "..", "elements"))
util_file_path = os.path.abspath(os.path.join(base_path, "..", "util"))
sys.path.append(elements_file_path)
sys.path.append(util_file_path)
from elements.list_element import List
from elements.button_element import Button
from util.locators import OverviewPageLocators


class OverviewPage(BasePage):

    def __init__(self, **kwargs):
        super(OverviewPage, self).__init__(**kwargs)

    def _validate_page(self, driver, config, **kwargs):
        url = driver.current_url
        # To normalize site links (because some of them httpS, other http)
        url = url.replace('https://', '').replace('http://', '')
        target_url = (config["site"]["url"] + kwargs.get("car_brand").lower().replace(' ', '-') +
                      "/" + kwargs.get("car_model").lower().replace(' ', '-') +
                      "/" + kwargs.get("car_year") + "/snapshot/").replace('https://', '').replace('http://', '')
        try:
            if url != target_url:
                raise Exception()
        except:
            raise InvalidPageException("Car Page not loaded")

    def get_engines_and_transmissions(self):
        # Get engines value
        available_engines_elements = List(OverviewPageLocators.AVAILABLE_ENGINES_LIST)
        # Delete first <li> element: <li> <strong>Available Engines:</strong> </li>
        engines_elements = available_engines_elements.elements[1:]
        engines = []
        for i in engines_elements:
            engines.append(i.text)

        # Get transmissions value
        available_transmissions_elements = List(OverviewPageLocators.AVAILABLE_TRANSMISSIONS_LIST)
        # Delete first <li> element: <li> <strong>Available Engines:</strong> </li>
        transmissions_elements = available_transmissions_elements.elements[1:]
        transmissions = []
        for i in transmissions_elements:
            transmissions.append(i.text)

        return (engines, transmissions)

    def compare(self):
        compare_button = Button(OverviewPageLocators.COMPARE_BUTTON)
        compare_button.click()

    def is_compare_possible(self):
        compare_button = Button(OverviewPageLocators.COMPARE_BUTTON)
        return not compare_button.missing

    def are_characteristics_present(self):
        available_engines_elements = List(OverviewPageLocators.AVAILABLE_ENGINES_LIST)
        available_transmissions_elements = List(OverviewPageLocators.AVAILABLE_TRANSMISSIONS_LIST)
        if available_engines_elements.missing == True and available_transmissions_elements.missing == True:
            return False
        else:
            return True
