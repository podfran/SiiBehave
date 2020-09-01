from behave import *
from faker import Faker

from pageobjects.registration_page import RegistrationPage


@given('a web browser is on the Sii store registration page')
def step_impl(context):
    context.reg_page = RegistrationPage().go_to()


@when('valid details are entered')
def step_impl(context):
    fake = Faker()
    context.reg_page.select_title_mrs()
    context.reg_page.enter_first_name(fake.first_name())
    context.reg_page.enter_last_name(fake.last_name())
    context.reg_page.enter_email_address(fake.email())
    context.reg_page.enter_password('12345678')
    context.result_page = context.reg_page.click_save()


@then('the user is logged in')
def step_impl(context):
    assert context.result_page.sign_out_link.is_visible()
