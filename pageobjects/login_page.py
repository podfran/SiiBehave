"""Login page object"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageobjects.customer_account_page import CustomerAccountPage
from pageobjects.store_page import SiiStorePage


class LoginPage(SiiStorePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.login_form = self.wait.until(
            expected_conditions.presence_of_element_located((
                By.ID, 'login-form'
            ))
        )

    def enter_email_address(self, email_address):
        email_address_field = self.login_form.find_element_by_css_selector(
            'input[type=email]'
        )
        email_address_field.send_keys(email_address)

    def enter_password(self, password):
        password_field = self.login_form.find_element_by_css_selector(
            'input[type=password]'
        )
        password_field.send_keys(password)

    def click_sign_in(self):
        signin_button = self.login_form.find_element_by_id(
            'submit-login'
        )
        signin_button.click()
        return CustomerAccountPage(self.driver)
