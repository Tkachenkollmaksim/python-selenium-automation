from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@then('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Side navigation product name not visible'
    )


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


# @then('Click on Add to Cart button')
# def side_nav_click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
#     sleep(3)


@then('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@then('Confirm Add to Cart button from side navigation')
def click_add_to_cart_side_bar(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(3)


#@then('Verify cart has {amount} item(s)')
def verify_add_to_cart(context):
    #Click Sign In
    context.driver.find_element(CART_SUMMARY).click()
    sleep(1)