from behave import *

from pageobjects.login_page import LoginPage


@given('a web browser is at the Sii store login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver).go_to()


@when('registered credentials are used')
def step_impl(context):
    context.login_page.enter_email_address('a1@gmail.com')
    context.login_page.enter_password('12345678')
    context.result_page = context.login_page.click_sign_in()
