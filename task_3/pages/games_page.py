# -*- coding: utf-8 -*-
from .base_page import BasePage
from .base_page import InvalidPageException
from selenium.webdriver import ActionChains
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import urllib.parse


class GamesPage(BasePage):

    def __init__(self, driver, data_controller, language):
        self.language = language
        super(GamesPage, self).__init__(driver, data_controller)

    def _validate_page(self, driver, data_controller):
        url = driver.current_url
        try:
            if urllib.parse.quote(
                    data_controller.config["site"]["locators"]["link_text"][self.language], safe='') not in url:
                raise Exception()
        except:
            raise InvalidPageException("Specified Page not loaded")

    def navigate_to_specials(self):
        # Navigate to Specials tab and click it
        specials_id = self.driver.find_element_by_id(self.data_controller.config["site"]["locators"]["specials_id"])
        navigate_to_specials = ActionChains(self.driver)
        navigate_to_specials.move_to_element_with_offset(specials_id, 5, 5)
        navigate_to_specials.click()
        navigate_to_specials.perform()

    def get_games_list_with_sales_and_click_target_game(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, self.data_controller.config["site"]["locators"]["games_xpath"])))

        app_ids = []

        # To prevent "Element not found in the cache" error, which happens
        # randomly because of DOM modifications use cycle with page refresh
        for attempt in range(10):
            try:
                games_elements = self.driver.find_elements_by_xpath(
                    self.data_controller.config["site"]["locators"]["games_xpath"])
                for i in games_elements:
                    # Check that current game is single
                    if i.get_attribute("data-ds-packageid") is None:
                        # Get app_id of current single game
                        app_id = i.get_attribute("data-ds-appid")
                        app_ids.append(app_id)
            except:
                self.driver.refresh()
            else:
                break

        # Get discounts values in text format
        discounts = []
        for i in app_ids:
            for attempt in range(10):
                try:
                    element_text = self.driver.find_element_by_xpath(
                        self.data_controller.config["site"]["locators"]["discount"]["part_1"] +
                        i +
                        self.data_controller.config["site"]["locators"]["discount"]["part_2"]).text
                    discounts.append(element_text)
                except:
                    self.driver.refresh()
                else:
                    break

        # Get discounts values using regular expression to leave only numbers
        # (without -, % and etc.)
        discounts_values = []
        for i in discounts:
            regexp = r'[^\d]'
            value = re.sub(regexp, '', i)  # TODO move regexp to config file
            if value != '':
                discounts_values.append(int(value))
            # If game has no discount paste 0 to discount value
            else:
                discounts_values.append(0)

        # Get dictionary with key = app_id; value = discount_value
        result = dict(zip(app_ids, discounts_values))

        # Get game app_id with max discount value
        target_app_id = max(result, key=result.get)

        target_game_discount = ""
        target_game_price = ""
        target_game_final_price = ""

        for attempt in range(10):
            try:
                target_game = self.driver.find_element_by_xpath(
                    self.data_controller.config["site"]["locators"]["target_game"]["part_1"] +
                    target_app_id +
                    self.data_controller.config["site"]["locators"]["target_game"]["part_2"])
                # Save discount, price and final price values of the target game
                target_game_discount = self.driver.find_element_by_xpath(
                    self.data_controller.config["site"]["locators"]["target_game_discount"]["part_1"] +
                    target_app_id +
                    self.data_controller.config["site"]["locators"]["target_game_discount"]["part_2"]).text
                target_game_price = self.driver.find_element_by_xpath(
                    self.data_controller.config["site"]["locators"]["target_game_price"]["part_1"] +
                    target_app_id +
                    self.data_controller.config["site"]["locators"]["target_game_price"]["part_2"]).text
                target_game_final_price = self.driver.find_element_by_xpath(
                    self.data_controller.config["site"]["locators"]["target_game_final_price"]["part_1"] +
                    target_app_id +
                    self.data_controller.config["site"]["locators"]["target_game_final_price"]["part_2"]).text

                # Navigate to target game and click it
                navigate_to_target_game = ActionChains(self.driver)
                navigate_to_target_game.move_to_element_with_offset(target_game, 5, 5)
                navigate_to_target_game.click()
                navigate_to_target_game.perform()
            except:
                self.driver.refresh()
            else:
                break

        return(target_app_id, target_game_discount, target_game_price, target_game_final_price)

    def check_is_age_validation_required(self, language):
        age_validation_element_text = self.driver.find_element_by_tag_name(
            self.data_controller.config["site"]["locators"]["tag_name"]).text
        if age_validation_element_text == \
                self.data_controller.config["site"]["locators"]["age_validation_text"][language]:
            return True
        else:
            return False
