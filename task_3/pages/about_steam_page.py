from .base_page import BasePage
from .base_page import InvalidPageException
import os
import time


class AboutSteamPage(BasePage):

    def __init__(self, driver, data_controller):
        super(AboutSteamPage, self).__init__(driver, data_controller)

    def _validate_page(self, driver, data_controller):
        url = driver.current_url
        try:
            if url != data_controller.config["site"]["about_steam_url"]:
                raise Exception()
        except:
            raise InvalidPageException("About Steam Page not loaded")

    def click_install_steam_to_download_steam_file(self):
        self.driver.find_element_by_id(
            self.data_controller.config["site"]["locators"]["install_steam_now_button_id"]).click()

    def check_file_downloading(self, dir):
        if not os.path.exists(dir + self.data_controller.config["steam_exe"]):
            time.sleep(5)
        # Check if file exists
        if os.path.isfile(dir + self.data_controller.config["steam_exe"]):
            # Completed if difference between current and last file modification times more than 5 seconds
            while True:
                # Return the time of last modification of path. The return value in seconds since the epoch
                last_file_modification_time = os.path.getmtime(dir + self.data_controller.config["steam_exe"])
                # Return the time in seconds since the epoch
                current_time = time.time()
                if last_file_modification_time < current_time + 5:
                    break
            print("File is downloaded!")
        else:
            raise Exception("File is not downloaded!")

        # To prevent error where Firefox has no time to remove SteamSetup.exe.part use sleep
        time.sleep(1)

