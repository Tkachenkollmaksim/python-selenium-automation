from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


#@then('Verify Cart Empty results shown')
def verify_cart_empty(context):
    # Verification
    actual_result = context.driver.find_element(By.CSS_SELECTOR, value="[data-test='boxEmptyMsg'] h1").text
    expected_result = 'Your cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result}, did not match {actual_result}'
    print('Test case Passed')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"




