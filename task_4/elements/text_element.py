from .base_element import BaseElement


class Text(BaseElement):

    def __init__(self, locator):
        super(Text, self).__init__(locator)

    def click(self):
        return

    def get_text(self):
        return self.element.text
