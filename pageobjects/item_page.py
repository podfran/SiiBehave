"""Item page object"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageobjects.store_page import SiiStorePage


class ItemPage(SiiStorePage):
    def __init__(self, driver):
        super(ItemPage, self).__init__(driver)
        self.cart_propt = None
        self.product_section = self.wait.until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//section[@itemtype="https://schema.org/Product"]'
            ))
        )

    @property
    def cart_items_count(self):
        items_count_element = self.driver.find_element_by_xpath('//span[@class="cart-products-count"]')
        return int(items_count_element.text.strip('()'))

    def add_to_cart(self):
        self.product_section.find_element_by_xpath('.//button[@type="submit"]').click()
        self.cart_propt = self.wait.until(
            expected_conditions.presence_of_element_located((
                By.ID, 'blockcart-modal'
            ))
        )

    def dismiss_prompt(self):
        self.cart_propt.find_element_by_xpath('.//*[@class="cart-content-btn"]/button').click()
        self.wait.until(
            expected_conditions.invisibility_of_element(
                self.cart_propt
            )
        )
