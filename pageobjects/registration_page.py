"""Registration page object."""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from pageobjects.main_page import MainPage
from pageobjects.store_page import SiiStorePage


class RegistrationPage(SiiStorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.registration_form = self.wait.until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'register-form'))
        )

    def select_title(self, title: str):
        if 'mrs' in title.lower():
            value = 2
        else:
            value = 1
        radio = self.registration_form.find_element_by_xpath(
            f'//input[@name="id_gender"][@value="{value}"]'
        )
        radio.click()

    def enter_first_name(self, first_name: str):
        first_name_field = self.registration_form.find_element_by_xpath(
            '//input[@name="firstname"]'
        )
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str):
        last_name_field = self.registration_form.find_element_by_xpath(
            '//input[@name="lastname"]'
        )
        last_name_field.send_keys(last_name)

    def enter_email_address(self, email_address: str):
        email_address_field = self.registration_form.find_element_by_xpath(
            '//input[@name="email"]'
        )
        email_address_field.send_keys(email_address)

    def enter_password(self, password: str):
        password_field = self.registration_form.find_element_by_xpath(
            '//input[@name="password"]'
        )
        password_field.send_keys(password)

    def click_save(self):
        self.registration_form.find_element_by_class_name('form-control-submit').click()
        return MainPage(self.driver)
