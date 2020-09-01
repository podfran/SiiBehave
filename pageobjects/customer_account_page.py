"""Customer account page object"""
from selenium.webdriver.common.by import By

from pageobjects.store_page import SiiStorePage
from pageobjects.uiobject import WebUIObject


class CustomerAccountPage(SiiStorePage):
    def __init__(self, driver):
        super(CustomerAccountPage, self).__init__(driver)
        self.page_header = WebUIObject(self.driver, By.CLASS_NAME, 'page-header')
