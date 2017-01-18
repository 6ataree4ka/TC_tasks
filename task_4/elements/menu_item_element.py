from .base_element import BaseElement


class MenuItem(BaseElement):

    def __init__(self, locator):
        super(MenuItem, self).__init__(locator)

    def click(self):
        self.element.click()
