# -*- coding: utf-8 -*-
import unittest, os
from base_test_case import BaseTestCase
from pages.main_page import MainPage
from pages.games_page import GamesPage
from pages.birth_date_page import BirthDatePage
from pages.sinlge_game_page import SingleGamePage
from pages.about_steam_page import AboutSteamPage


class SteamTest(BaseTestCase):

    def test_steam_with_selecting_game_with_max_discount_and_downloading_steam_file(self):
        # If you want to check steam_test on Russian version of Steam,
        # uncomment time.sleep(10), run test and change language to Russian on the main Steam page during sleep time
        # time.sleep(10)

        main_page = MainPage(self.driver, self.data_controller)
        language = main_page.check_language()
        main_page.browse_tab()
        self.driver.implicitly_wait(self.data_controller.config["wait"])
        main_page.select_item(language)
        self.driver.implicitly_wait(self.data_controller.config["wait"])

        games_page = GamesPage(self.driver, self.data_controller, language)
        title = self.driver.title
        self.assertEqual(self.data_controller.config["site"]["title"][language], title)

        games_page.navigate_to_specials()
        res = list(games_page.get_games_list_with_sales_and_click_target_game())
        self.driver.implicitly_wait(self.data_controller.config["wait"])

        if games_page.check_is_age_validation_required(language) == True:
            birth_page = BirthDatePage(self.driver, self.data_controller, language)
            birth_page.enter_birth_date()
        self.driver.implicitly_wait(self.data_controller.config["wait"])

        single_game_page = SingleGamePage(self.driver, self.data_controller, res[0])
        single_game_page._validate_page(self.driver, self.data_controller)
        single_game_page.check_discount_and_price_values(res[1], res[2], res[3])
        single_game_page.find_and_click_install_steam_button()
        self.driver.implicitly_wait(self.data_controller.config["wait"])

        about_steam_page = AboutSteamPage(self.driver, self.data_controller)
        about_steam_page.click_install_steam_to_download_steam_file()
        about_steam_page.check_file_downloading(os.path.dirname(__file__))

if __name__ == "__main__":
    unittest.main()
