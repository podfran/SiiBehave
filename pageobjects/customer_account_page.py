"""Customer account page object"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageobjects.store_page import SiiStorePage


class CustomerAccountPage(SiiStorePage):
    def __init__(self, driver):
        super(CustomerAccountPage, self).__init__(driver)
        self.wait.until(
            expected_conditions.presence_of_element_located((
                By.CLASS_NAME, 'page-header'
            ))
        )
