"""Registration page object."""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from pageobjects.main_page import MainPage
from pageobjects.common import WebUIObject, BasePage


class RegistrationPage(BasePage):
    page_url = 'http://5.196.7.235/login?create_account=1'

    def __init__(self):
        super().__init__()
        # The following two should - I think - reference the input object and not the span, but they don't
        self.mr_radio = WebUIObject(By.XPATH, '//span[input/@value="1"]')
        self.mrs_radio = WebUIObject(By.XPATH, '//span[input/@value="2"]')
        self.first_name_field = WebUIObject(By.NAME, 'firstname')
        self.last_name_field = WebUIObject(By.NAME, 'lastname')
        self.email_address_field = WebUIObject(By.NAME, 'email')
        self.password_field = WebUIObject(By.NAME, 'password')
        self.save_button = WebUIObject(By.CLASS_NAME, 'form-control-submit')

    def select_title_mrs(self):
        self.mrs_radio.click()

    def select_title_mr(self):
        self.mr_radio.click()

    def enter_first_name(self, first_name: str):
        self.first_name_field.type(first_name)

    def enter_last_name(self, last_name: str):
        self.last_name_field.type(last_name)

    def enter_email_address(self, email_address: str):
        self.email_address_field.type(email_address)

    def enter_password(self, password: str):
        self.password_field.type(password)

    def click_save(self):
        self.save_button.click()
        return MainPage()
