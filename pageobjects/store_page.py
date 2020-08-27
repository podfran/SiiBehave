"""Generic store page"""
from selenium.webdriver.support.ui import WebDriverWait


class SiiStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
