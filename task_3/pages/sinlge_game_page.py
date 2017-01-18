from .base_page import BasePage
from .base_page import InvalidPageException


class SingleGamePage(BasePage):

    def __init__(self, driver, data_controller, target_app_id):
        self.app_id = target_app_id
        super(SingleGamePage, self).__init__(driver, data_controller)

    def _validate_page(self, driver, data_controller):
        url = driver.current_url
        try:
            if self.app_id not in url:
                raise Exception()
        except:
            raise InvalidPageException("Target Game Page not loaded")

    def check_discount_and_price_values(
            self, target_game_discount, target_game_price, target_game_final_price):

        discount = self.driver.find_element_by_class_name(
            self.data_controller.config["site"]["locators"]["discount_class_name"]).text
        price = self.driver.find_element_by_class_name(
            self.data_controller.config["site"]["locators"]["price"]).text
        final_price = self.driver.find_element_by_class_name(
            self.data_controller.config["site"]["locators"]["final_price"]).text

        if discount != target_game_discount or price != target_game_price \
                or final_price[:-4] != target_game_final_price:  # Use [:-4] to remove the extra characters " USD"
            raise Exception("Game discount, price or final price is not valid")

    def find_and_click_install_steam_button(self):
        self.driver.find_element_by_class_name(
            self.data_controller.config["site"]["locators"]["install_steam_button"]).click()
