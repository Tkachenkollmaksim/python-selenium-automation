from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#@given('Open the target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(1)


@given('Open Target-Circle')
def open_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(1)


#@when('Search for {item}')
def search_product(context, item):
    #Search Field - Enter text
    context.driver.find_element(By.ID, value='search').send_keys(item)
    #After Text - Click Search
    context.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()
    sleep(1) # Wait for page to load


#@when('Click on Cart icon')
def click_cart(context):
    #Click Cart
    context.driver.find_element(By.CSS_SELECTOR, value="[data-test='@web/CartLink']").click()
    sleep(5) # Wait for page to load


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