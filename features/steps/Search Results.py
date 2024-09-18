from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, value="[id*='addToCartButtonOrTextIdFor']").click()
    sleep(1)
