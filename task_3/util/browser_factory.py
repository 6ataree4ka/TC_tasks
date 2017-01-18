from selenium import webdriver


class BrowserFactory(object):

    def __init__(self, data_controller, dir):
        browser = data_controller.config["browser"]

        # Select browser (chrome/firefox are possible values)
        if browser == "chrome":
            # Get Chrome driver
            chrome_driver_path = dir + \
                data_controller.config["drivers"]["chrome"]
            # Set Chrome profile to disable safebrowsing and set download path
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory" : dir + data_controller.config["downloads_dir"],
                     "safebrowsing.enabled": "false"}
            chromeOptions.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(chrome_driver_path, chrome_options=chromeOptions)

        elif browser == "firefox":
            fp = webdriver.FirefoxProfile()
            # Set Firefox profile to disable dialogs and set download path
            fp.set_preference("browser.download.folderList", 2)
            fp.set_preference("browser.download.manager.showWhenStarting", False)
            fp.set_preference("browser.download.dir", dir + data_controller.config["downloads_dir"])
            fp.set_preference("browser.helperApps.alwaysAsk.force", False)
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            self.driver = webdriver.Firefox(firefox_profile=fp)

        else:
            self.driver = webdriver.Firefox()
