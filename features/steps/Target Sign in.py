from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')
#    sleep(5)

@when('Click Sign In')
def search_product(context):
    #Click Sign In
    context.driver.find_element(By.CSS_SELECTOR, value='.sc-58ad44c0-3.kwbrXj.h-margin-r-x3').click()
#    sleep(5) # Wait for page to load

@then('From right side navigation menu, click Sign In')
def search_product(context):
    #Click Sign In from the right pop-up
    context.driver.find_element(By.CSS_SELECTOR, value='.sc-859e7637-0.hHZPQy').click()
 #   sleep(5) # Wait for page to load

@then('Verify Sign In form opened')
def verify_results(context):
    # Verification
    actual_result = context.driver.find_element(By.CSS_SELECTOR, value='.sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs').text
    expected_result = 'Sign into your Target account'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    print('Test case Passed')

    context.driver.quit()
