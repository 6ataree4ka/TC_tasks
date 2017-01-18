import unittest
import os.path
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class OnlinerTest(unittest.TestCase):

    def setUp(self):
        # Read settings from file
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'settings.txt')
        file = open(filename)
        self.login = file.readline()  # First line is username
        self.password = file.readline()  # Second line is password
        # Third line is browser (chrome/firefox/ie are possible values)
        self.browser = file.readline().lower()

        if self.browser == "chrome":
            dir = os.path.dirname(__file__)
            chrome_driver_path = dir + "\chromedriver.exe"
            self.driver = webdriver.Chrome(chrome_driver_path)
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "ie":
            dir = os.path.dirname(__file__)
            ie_driver_path = dir + "\IEDriverServer.exe"
            self.driver = webdriver.Ie(ie_driver_path)
        else:
            self.driver = webdriver.Firefox()

        # Implicit wait 30 seconds
        self.driver.implicitly_wait(30)

        self.driver.maximize_window()
        self.driver.get('http://www.onliner.by')

    def test_open_onliner(self):
        driver = self.driver
        self.assertEqual('Onliner.by', driver.title)

    def test_login_logout_user(self):
        driver = self.driver

        # Simulating Fluent wait like in Java
        fluent_wait = WebDriverWait(
            driver, 30, poll_frequency=1, ignored_exceptions=[
                ElementNotVisibleException, ElementNotSelectableException])
        login_button = fluent_wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "auth-bar__item--text")))
        login_button.click()

        # Enter credentials
        login_field = driver.find_elements_by_xpath(
            "*//div/input[@type='text']")
        # Check placeholder of login field (to use getAttribute(-) in accordance with home_task)
        # В задании должны быть использованы методы click, sendKeys,
        # getText/Text, getAttribute местами это может быть неуместно, но важно
        # продемонстрировать работу с ними
        self.assertEqual(
            "Ник или e-mail",
            login_field[0].get_attribute("placeholder"))
        login_field[0].send_keys(self.login)

        password_field = driver.find_elements_by_xpath(
            "*//div/input[@type='password']")
        password_field[0].send_keys(self.password)

        login_form_button = driver.find_elements_by_xpath(
            "*//div/button[@type='submit']")[0]
        login_action = ActionChains(driver)
        login_action.move_to_element_with_offset(login_form_button, 5, 5)
        login_action.click()
        login_action.perform()

        # WebDriverWait in combination with ExpectedCondition (Explicit Wait)
        logout_wait = WebDriverWait(driver, 30)
        logout_button = logout_wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "exit")))

        self.assertEqual("Выйти", logout_button.text)
        logout_button.click()

        login_wait = WebDriverWait(driver, 30)
        login_button = login_wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "auth-bar__item--text")))
        self.assertEqual("Вход", login_button.text)

    def test_get_themes_list_and_open_random(self):
        driver = self.driver

        # Get themes list as WebElement objects
        theme_elem = driver.find_elements_by_css_selector(
            'span.project-navigation__sign')
        themes = []

        # Filling themes
        for i in range(0, len(theme_elem)):
            if theme_elem[i].text != '':
                themes.append(theme_elem[i])

        # Select random theme
        random_element = random.sample(themes, 1)[0]
        random_element_text = random_element.text

        # Actions(MouseClick)
        action = ActionChains(driver)
        action.move_to_element_with_offset(random_element, 5, 5)
        action.click()
        action.perform()

        theme_title = driver.find_element_by_class_name("schema-header__title")
        self.assertEqual(random_element_text, theme_title.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
