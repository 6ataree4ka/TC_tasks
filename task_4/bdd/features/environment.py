import sys
import os
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "..", "util"))
sys.path.append(file_path)
from util.browser_factory import BrowserFactory
from util.data_controller import DataController

def before_all(context):
    context.driver = BrowserFactory.instance().driver
    context.configuration = DataController.instance().config

    context.driver.implicitly_wait(context.configuration["wait"])
    context.driver.maximize_window()
    context.driver.get(context.configuration["site"]["url"])

def after_all(context):
    context.driver.quit()