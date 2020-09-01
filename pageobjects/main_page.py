"""Main page object"""
from selenium.webdriver.common.by import By

from pageobjects.item_page import ItemPage
from pageobjects.common import WebUIObject, BasePage


class MainPage(BasePage):
    page_url = 'http://5.196.7.235/'

    def __init__(self):
        super().__init__()
        self.customer_account_link = WebUIObject(By.CLASS_NAME, 'account')

    def click_popular_item(self, number):
        pop_prods = self.driver.find_elements_by_tag_name('article')
        pop_prods[number - 1].click()
        return ItemPage(self.driver)
