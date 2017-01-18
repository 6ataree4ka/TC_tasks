from selenium.webdriver.common.by import By


class MainPageLocators(object):
    BUY_BUTTON = (By.XPATH, ".//*[@title='Buy']")
    REVIEW_CAR_MENU_ITEM = (By.XPATH, ".//*[@url='/reviews/']")


class ReviewPageLocators(object):
    MAKE_DROPDOWN = (By.ID, "makeid")
    MODEL_DROPDOWN = (By.ID, "modelid")
    YEAR_DROPDOWN = (By.ID, "year")
    GO_BUTTON = (By.CLASS_NAME, "col3")


class CarPageLocators(object):
    OVERVIEW_TAB = (By.XPATH, ".//a[text()='Overview']")


class OverviewPageLocators(object):
    AVAILABLE_ENGINES_LIST = (
        By.XPATH, ".//*[@class='col13']/*[@class='list-nobullets']/li")
    AVAILABLE_TRANSMISSIONS_LIST = (
        By.XPATH, ".//*[@class='col10']/*[@class='list-nobullets']/li")
    COMPARE_BUTTON = (By.ID, "comparesbs")


class ComparePageLocators(object):
    COMPARE_TITLE_TEXT = (By.TAG_NAME, "h1")
    YEAR_DROPDOWN = (By.ID, "year")
    MAKE_DROPDOWN = (By.ID, "division")
    MODEL_DROPDOWN = (By.ID, "model")
    COMPARE_BUTTON = (By.XPATH, ".//a[text()='Compare']")
    FIRST_CAR_ENGINES_LIST = (
        By.XPATH, ".//td[text()='Available Engines']/../*")
    SECOND_CAR_ENGINES_LIST = (
        By.XPATH, ".//td[text()='Available Engines']/../*")
    FIRST_CAR_TRANSMISSIONS_LIST = (
        By.XPATH, ".//td[text()='Available Transmissions']/../*")
    SECOND_CAR_TRANSMISSIONS_LIST = (
        By.XPATH, ".//td[text()='Available Transmissions']/../*")
