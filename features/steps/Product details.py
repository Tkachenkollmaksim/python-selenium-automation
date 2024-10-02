from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_cart(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['grey, dark khaki, navy/tan, stone/grey, white/gum, white/navy/red, white/sand/tan, black/gum - Out of Stock ']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for color in colors:
        print(color)
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current text color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print('actual_color list', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match {actual_colors}'




