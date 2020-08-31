"""Main page object"""
from selenium.webdriver.common.by import By

from pageobjects.item_page import ItemPage
from pageobjects.store_page import SiiStorePage
from pageobjects.uiobject import WebUIObject


class MainPage(SiiStorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.customer_account_link = WebUIObject(self.driver, By.CLASS_NAME, 'account')

    def click_popular_item(self, number):
        pop_prods = self.driver.find_elements_by_tag_name('article')
        pop_prods[number - 1].click()
        return ItemPage(self.driver)
