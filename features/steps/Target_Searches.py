from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open the target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(1)


@when('Search for {item}')
def search_product(context, item):
    #Search Field - Enter text
    context.driver.find_element(By.ID, value='search').send_keys(item)
    #After Text - Click Search
    context.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()
    sleep(1) # Wait for page to load


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    # Verification
    actual_result = context.driver.find_element(By.XPATH, value="//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product}, got actual {actual_result}'

