from behave import *

from pageobjects.main_page import MainPage


@given('a web browser is at the home page')
def step_impl(context):
    context.driver.get('http://5.196.7.235/')
    context.main_page = MainPage(context.driver)


@given('no items are in cart')
def step_impl(context):
    assert context.main_page.cart_items_count == 0


@when('item from popular products is chosen')
def step_impl(context):
    context.item_page = context.main_page.click_popular_item(1)


@when('item is added to cart')
def step_impl(context):
    context.item_page.add_to_cart()
    context.item_page.dismiss_prompt()


@then('cart count increases')
def step_impl(context):
    assert context.item_page.cart_items_count == 1
