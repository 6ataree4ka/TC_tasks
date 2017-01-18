from .base_element import BaseElement
import random
from selenium.webdriver.support.ui import Select


class Dropdown(BaseElement):

    def __init__(self, locator):
        super(Dropdown, self).__init__(locator)

    def click(self):
        return

    # Select random option from dropdown except first option with Dropdown Name Text
    def select_random_option(self, **kwargs):
        select = Select(self.element)
        options = select.options
        options_texts = []
        for i in options:
            options_texts.append(i.text)
        if kwargs.get("without_first") == True:
            random_text = random.choice(options_texts[1:])
        else:
            random_text = random.choice(options_texts)
        select.select_by_visible_text(random_text)
        return random_text

    def select_target_option(self, option):
        select = Select(self.element)
        select.select_by_visible_text(option)

    def get_selected_option(self):
        select = Select(self.element)
        return select.first_selected_option.text
