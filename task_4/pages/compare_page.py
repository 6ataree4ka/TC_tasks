from .base_page import BasePage
from .base_page import InvalidPageException

import sys
import os
base_path = os.path.dirname(__file__)
elements_file_path = os.path.abspath(os.path.join(base_path, "..", "elements"))
util_file_path = os.path.abspath(os.path.join(base_path, "..", "util"))
sys.path.append(elements_file_path)
sys.path.append(util_file_path)
from elements.text_element import Text
from elements.dropdown_element import Dropdown
from elements.button_element import Button
from elements.list_element import List
from util.locators import ComparePageLocators


class ComparePage(BasePage):

    def __init__(self, **kwargs):
        super(ComparePage, self).__init__(**kwargs)

    def _validate_page(self, driver, config, **kwargs):
        compare_title = Text(ComparePageLocators.COMPARE_TITLE_TEXT).get_text()
        try:
            if compare_title != "Compare":
                raise Exception()
        except:
            raise InvalidPageException("Compare Page not loaded")

    def select_necessary_car(self, brand, model, year):
        try:
            # Select year
            year_element = Dropdown(ComparePageLocators.YEAR_DROPDOWN)
            year_element.select_target_option(year)

            # Select brand
            make_element = Dropdown(ComparePageLocators.MAKE_DROPDOWN)
            make_element.select_target_option(brand)
            selected_make_option = make_element.get_selected_option()

            # To prevent the difference in the brand names because of different registers (e.g. BMW - bmw)
            attempts = 0
            while selected_make_option == "Select a Make":
                attempts += 1
                make_element.select_target_option(brand)
                selected_make_option = make_element.get_selected_option()
                if brand.islower():
                    brand = brand.upper()
                elif brand.isupper():
                    brand = brand.lower()
                else:
                    brand = brand.lower()
                if attempts > 5:
                    break

            # Select model
            model_element = Dropdown(ComparePageLocators.MODEL_DROPDOWN)
            model_element.select_target_option(model)
            selected_model_option = model_element.get_selected_option()

            # To prevent the difference in the model names because of different registers (e.g. ForTwo - fortwo)
            attempts = 0
            while selected_model_option == "Select a Model":
                attempts += 1
                model_element.select_target_option(model)
                selected_model_option = model_element.get_selected_option()
                if model.islower():
                    model = model.upper()
                elif model.isupper():
                    model = model.lower()
                else:
                    model = model.lower()
                if attempts > 5:
                    break

            compare_button = Button(ComparePageLocators.COMPARE_BUTTON)
            compare_button.click()
        except:
            raise Exception("Target Make or Model not found on the page!")

    def get_car_parameters(self):
        first_car_engines = List(ComparePageLocators.FIRST_CAR_ENGINES_LIST).elements[2].text.split("\n")
        second_car_engines = List(ComparePageLocators.SECOND_CAR_ENGINES_LIST).elements[1].text.split("\n")

        first_car_transmissions = List(ComparePageLocators.FIRST_CAR_TRANSMISSIONS_LIST).elements[2].text.split("\n")
        second_car_transmissions = List(ComparePageLocators.SECOND_CAR_TRANSMISSIONS_LIST).elements[1].text.split("\n")

        return (first_car_engines, second_car_engines, first_car_transmissions, second_car_transmissions)

    def normalize_data(self, value):
        for i, s in enumerate(value):
            value[i] = s.lower().replace(',', '').replace('speed', 'spd').replace('manual', 'man')
        return value

    def compare_car_parameters(self, first_car, second_car, first_car_engines, second_car_engines,
                               first_car_transmissions, second_car_transmissions):

        if self.normalize_data(first_car.engines) == self.normalize_data(first_car_engines) \
                and self.normalize_data(first_car.transmissions) == self.normalize_data(first_car_transmissions) \
                and self.normalize_data(second_car.engines) == self.normalize_data(second_car_engines) \
                and self.normalize_data(second_car.transmissions) == self.normalize_data(second_car_transmissions):
            print("Cars have been compared and parameters are the same!")
        else:
            raise Exception("Car parameters do not match!")
