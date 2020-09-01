"""Customer account page object"""
from selenium.webdriver.common.by import By

from pageobjects.common import WebUIObject, BasePage


class CustomerAccountPage(BasePage):
    def __init__(self, driver):
        super(CustomerAccountPage, self).__init__()
        self.page_header = WebUIObject(By.CLASS_NAME, 'page-header')
