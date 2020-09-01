"""Generic store page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pageobjects.uiobject import WebUIObject, Browser


class SiiStorePage(Browser):
    page_url = None

    def __init__(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.cart_count_object = WebUIObject(By.CLASS_NAME, 'cart-products-count')
        self.sign_out_link = WebUIObject(By.CLASS_NAME, 'logout')

    @property
    def cart_items_count(self) -> int:
        return int(self.cart_count_object.text.strip('()'))

    def go_to(self):
        self.driver.get(self.page_url)
        return self
