import random
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from base_test_case import BaseTestCase
from home_page import HomePage
from login_page import LoginPage
import re
import os


class OnlinerTest(BaseTestCase):

    def test_login_logout_user(self):
        # Simulating Fluent wait like in Java
        fluent_wait = WebDriverWait(
            self.driver, 30, poll_frequency=1, ignored_exceptions=[
                ElementNotVisibleException, ElementNotSelectableException])
        login_button = fluent_wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "auth-bar__item--text")))
        login_button.click()

        login_page = LoginPage(self.driver)
        login_page._validate_page(self.driver)
        login_page.input_login(self.login)
        login_page.input_password(self.password)
        login_page.submit_credentials()

        # WebDriverWait in combination with ExpectedCondition (Explicit Wait)
        logout_wait = WebDriverWait(self.driver, 30)
        logout_button = logout_wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "exit")))

        self.assertEqual("Выйти", logout_button.text)
        logout_button.click()

        login_wait = WebDriverWait(self.driver, 30)
        login_button = login_wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "auth-bar__item--text")))
        self.assertEqual("Вход", login_button.text)

    def test_get_themes_list_and_open_random(self):
        home_page = HomePage(self.driver)
        home_page._validate_page(self.driver)

        themes = home_page.find_all_themes()
        # Select random theme
        random_element = random.sample(themes, 1)[0]
        random_element_text = random_element.text

        # Actions(MouseClick)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(random_element, 5, 5)
        action.click()
        action.perform()

        theme_title = self.driver.find_element_by_class_name(
            "schema-header__title")
        self.assertEqual(random_element_text, theme_title.text)

    def test_get_catalog_list_using_reg_exp_write_to_csv(self):
        self.driver.get("http://catalog.onliner.by/")
        page = self.driver.page_source
        pattern = re.compile(
            r'<h3 class="b-tile-header max-lines-2" style="float: none; position: static;">(.*?)</h3>',
            re.S)
        result = re.findall(pattern, page)
        self.data_controller.write_data(self.output_dir, result)
        self.assertTrue(os.path.exists(self.output_dir))

if __name__ == "__main__":
    unittest.main()
