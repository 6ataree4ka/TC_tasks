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
from elements.dropdown_element import Dropdown
from util.locators import ReviewPageLocators


class ReviewPage(BasePage):

    def __init__(self, **kwargs):
        super(ReviewPage, self).__init__(**kwargs)

    def _validate_page(self, driver, config, **kwargs):
        url = driver.current_url
        # To normalize site links (because some of them httpS, other http)
        url = url.replace('https://', '').replace('http://', '')
        target_url = (config["site"]["url"] + "reviews/").replace('https://', '').replace('http://', '')
        try:
            if url != target_url:
                raise Exception()
        except:
            raise InvalidPageException("Review Page not loaded")

    def select_random_car(self):
        car_brand = ''
        car_model = ''
        car_year = 0

        # To prevent 'Compare' button missing (some old cars don't have Compare button)
        while int(car_year) < 2000:
            # Select brand
            make = Dropdown(ReviewPageLocators.MAKE_DROPDOWN)
            car_brand = make.select_random_option(without_first=True)
            # Select model
            model = Dropdown(ReviewPageLocators.MODEL_DROPDOWN)
            car_model = model.select_random_option(without_first=True)
            # Select year
            year = Dropdown(ReviewPageLocators.YEAR_DROPDOWN)
            car_year = year.select_random_option()

        return (car_brand, car_model, car_year)

    def view_car(self):
        go_button = Button(ReviewPageLocators.GO_BUTTON)
        go_button.click()