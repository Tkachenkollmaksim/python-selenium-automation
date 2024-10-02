from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Cart Empty results shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()