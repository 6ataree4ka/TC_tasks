from .base_element import BaseElement


class Button(BaseElement):

    def __init__(self, locator):
        super(Button, self).__init__(locator)

    def click(self):
        self.element.click()
