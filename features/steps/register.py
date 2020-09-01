from behave import *

from pageobjects.registration_page import RegistrationPage


@given('a web browser is on the Sii store registration page')
def step_impl(context):
    context.driver.get('http://5.196.7.235/login?create_account=1')
    context.reg_page = RegistrationPage(context.driver)


@when('valid details are entered')
def step_impl(context):
    context.reg_page.select_title_mrs()
    context.reg_page.enter_first_name('Amelia')
    context.reg_page.enter_last_name('Pond')
    context.reg_page.enter_email_address('a8@gmail.com')
    context.reg_page.enter_password('12345678')
    context.result_page = context.reg_page.click_save()


@then('the user is logged in')
def step_impl(context):
    assert context.result_page.sign_out_link.is_visible()
