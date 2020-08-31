"""Generic store page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pageobjects.uiobject import WebUIObject


class SiiStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.cart_count_object = WebUIObject(self.driver, By.CLASS_NAME, 'cart-products-count')

    @property
    def cart_items_count(self) -> int:
        return int(self.cart_count_object.text.strip('()'))
