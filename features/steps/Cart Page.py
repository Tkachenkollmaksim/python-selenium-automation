from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('View the cart')
def verify_cart_product(context):
    context.driver.find_element(By.CSS_SELECTOR, value=".sc-93ec7147-3.fUVkzh").text
    print('Test case Passed')