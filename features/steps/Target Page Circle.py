from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when('Search for Benefit')
def find_cell(context):
   #Benefit cells
   context.driver.find_element(By.CSS_SELECTOR, value="[data-test='@web/slingshot-components/CellsComponent/Link']")
   sleep(2)


@then('Verify that there are {expected_amount} benefit cells')
def verify_results(context, expected_amount):
    expected_amount = int(expected_amount)
    Links = context.driver.find_element(By.CSS_SELECTOR, value="[data-test*='@web/slingshot-components/CellsComponent/Link']").text
    assert len(Links) == expected_amount, F'Expected {expected_amount} links but got {len(Links)}'