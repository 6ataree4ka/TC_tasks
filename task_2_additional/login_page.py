from base_page import BasePage
from base_page import InvalidPageException
from selenium.webdriver import ActionChains


class LoginPage(BasePage):
    _login_page_submit_button_locator = "*//div/button[@type='submit']"

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_xpath(
                self._login_page_submit_button_locator)
        except:
            raise InvalidPageException("Login Page not loaded")

    def input_login(self, login):
        login_field = self.driver.find_elements_by_xpath(
            "*//div/input[@type='text']")
        login_field[0].send_keys(login)

    def input_password(self, password):
        password_field = self.driver.find_elements_by_xpath(
            "*//div/input[@type='password']")
        password_field[0].send_keys(password)

    def submit_credentials(self):
        login_form_button = self.driver.find_elements_by_xpath(
            "*//div/button[@type='submit']")[0]
        login_action = ActionChains(self.driver)
        login_action.move_to_element_with_offset(login_form_button, 5, 5)
        login_action.click()
        login_action.perform()
