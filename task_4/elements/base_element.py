from abc import abstractmethod

import sys
import os
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "util"))
sys.path.append(file_path)
from util.browser_factory import BrowserFactory


class BaseElement(object):

    def __init__(self, locator, **kwargs):
        self._find(locator, **kwargs)

    def _find(self, locator, **kwargs):
        try:
            if kwargs.get("multiple") == True:
                self.elements = BrowserFactory.instance().driver.find_elements(locator[0], locator[1])
            else:
                self.element = BrowserFactory.instance().driver.find_element(locator[0], locator[1])
            self.missing = False
        except:
            self.missing = True

    @abstractmethod
    def click(self):
        return
