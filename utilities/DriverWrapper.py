import os

from selenium import webdriver

import WebDrivers
from utilities import settings


class DriverWrapper:
    _instance = None

    @classmethod
    def get_driwer(cls):
        if not cls._instance:
            cls._instance = DriverWrapper()
            cls._driver = cls._instance._driver
        return cls._driver

    def __init__(self):
        webdriver_path = os.path.dirname(WebDrivers.__file__)
        options = webdriver.ChromeOptions()
        drivers_path = os.path.join(webdriver_path, "chromedriver.exe")
        self._driver = webdriver.Chrome(executable_path=drivers_path, chrome_options=options)
        self._driver.set_page_load_timeout(60)

    @classmethod
    def close_driver(cls):
        cls._driver.close()
        cls._driver.quit()
        cls._instance = None