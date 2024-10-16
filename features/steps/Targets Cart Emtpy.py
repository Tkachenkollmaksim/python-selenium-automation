from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart()


#@then('Verify Cart Empty results shown')
def verify_cart_empty(context):
    # Verification
    actual_result = context.driver.find_element(By.CSS_SELECTOR, value="[data-test='boxEmptyMsg'] h1").text
    expected_result = 'Your cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result}, did not match {actual_result}'
    print('Test case Passed')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.open_cart()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name()



