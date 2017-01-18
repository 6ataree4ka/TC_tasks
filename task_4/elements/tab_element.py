from .base_element import BaseElement


class Tab(BaseElement):

    def __init__(self, locator):
        super(Tab, self).__init__(locator)

    def click(self):
        self.element.click()
