from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('Click on Cart icon')
def click_cart(context):
    #Click Cart
    context.driver.find_element(By.CSS_SELECTOR, value="[data-test='@web/CartLink']").click()
    sleep(5) # Wait for page to load

@then('Verify Cart Empty results shown')
def verify_cart_empty(context):
    # Verification
    actual_result = context.driver.find_element(By.CSS_SELECTOR, value="[data-test='boxEmptyMsg'] h1").text
    expected_result = 'Your cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result}, did not match {actual_result}'
    print('Test case Passed')

