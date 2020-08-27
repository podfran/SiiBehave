"""Main page object"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageobjects.item_page import ItemPage
from pageobjects.store_page import SiiStorePage


class MainPage(SiiStorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//img[@alt="TesterSii"]'
            ))
        )

    @property
    def customer_account_link(self):
        return self.driver.find_element_by_class_name('account')

    @property
    def cart_items_count(self):
        items_count_element = self.driver.find_element_by_css_selector('span.cart-products-count')
        return int(items_count_element.text.strip('()'))

    def click_popular_item(self, number):
        pop_prods = self.driver.find_elements_by_tag_name('article')
        pop_prods[number - 1].click()
        return ItemPage(self.driver)
