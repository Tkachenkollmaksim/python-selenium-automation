from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open the target.com')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    sleep(1)
    context.app.main_page.open_main()

@given('Open Target-Circle')
def open_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(1)


# @when('Search for {item}')
# def search_product(context, item):
#     context.app.header.search_product(item)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


#@when('Click on Circle Tab')
def click_cart(context):
    #Click Cart
    context.driver.find_element(By.CSS_SELECTOR, value="[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle'']").click()
    sleep(1) # Wait for page to load


#@when('Click Sign In')
def search_product(context):
    #Click Sign In
    context.driver.find_element(By.CSS_SELECTOR, value='.sc-58ad44c0-3.kwbrXj.h-margin-r-x3').click()
#    sleep(5) # Wait for page to load


