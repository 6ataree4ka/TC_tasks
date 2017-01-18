from .base_element import BaseElement


class List(BaseElement):

    def __init__(self, locator):
        super(List, self).__init__(locator, multiple=True)

    def click(self):
        return
