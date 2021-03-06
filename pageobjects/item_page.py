"""Item page object"""
from selenium.webdriver.common.by import By

from pageobjects.common import WebUIObject, BasePage


class ItemPage(BasePage):
    def __init__(self, driver):
        super(ItemPage, self).__init__()
        self.add_to_cart_button = WebUIObject(By.CLASS_NAME, 'add-to-cart')
        self.continue_shopping_button = WebUIObject(By.XPATH, '//button[contains(text(), "Continue")]')

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def dismiss_prompt(self):
        self.continue_shopping_button.click()
