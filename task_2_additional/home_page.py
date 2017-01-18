from base_page import BasePage
from base_page import InvalidPageException


class HomePage(BasePage):
    _home_page_themes_navigation_locator = "project-navigation__flex"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name(
                self._home_page_themes_navigation_locator)
        except:
            raise InvalidPageException("Home Page not loaded")

    def find_all_themes(self):
        # Get themes list as WebElement objects
        theme_elem = self.driver.find_elements_by_css_selector(
            'span.project-navigation__sign')
        themes = []

        # Filling themes
        for i in range(0, len(theme_elem)):
            if theme_elem[i].text != '':
                themes.append(theme_elem[i])

        return themes
