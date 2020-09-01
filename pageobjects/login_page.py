"""Login page object"""
from selenium.webdriver.common.by import By

from pageobjects.customer_account_page import CustomerAccountPage
from pageobjects.store_page import SiiStorePage
from pageobjects.uiobject import WebUIObject


class LoginPage(SiiStorePage):
    page_url = 'http://5.196.7.235/login'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.email_address_field = WebUIObject(self.driver, By.NAME, 'email')
        self.password_field = WebUIObject(self.driver, By.NAME, 'password')
        self.sign_in_button = WebUIObject(self.driver, By.ID, 'submit-login')

    def enter_email_address(self, email_address):
        self.email_address_field.type(email_address)

    def enter_password(self, password):
        self.password_field.type(password)

    def click_sign_in(self):
        self.sign_in_button.click()
        return CustomerAccountPage(self.driver)
