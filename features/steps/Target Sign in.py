from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


NAV_SIGN_IN = (By.CSS_SELECTOR, '.sc-859e7637-0.hHZPQy')

@given('Open target.com')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@given('Open sign in page')
def open_sign_in(context):
    context.app.sign_in.open_sign_in()

@when('Click Nav Sign In')
def click_nav_sign_in(context):
    context.app.sign_in.click_nav_sign_in()

@when('Enter {text} for email')
def incorrect_email(context, text):
    sleep(5)
    context.app.sign_in.incorrect_email(text)

@when('Enter {input} for password')
def incorrect_pass(context, input):
    context.app.sign_in.incorrect_pass(input)

@then('Click Sign In button')
def click_sign_in_button(context):
    context.app.sign_in.click_sign_in_button()

@when('Store original window')
def store_window(context):
    context.original_window = context.app.sign_in.get_current_window()
    print('Original window: ', context.original_window)

@then('From right side navigation menu, click Sign In')
def nav_sign_in(context):
    # #Click Sign In from the right pop-up
    # context.driver.find_element(*NAV_SIGN_IN).click()
 #   sleep(5) # Wait for page to load
    context.app.header.nav_sign_in()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    # Verification
    context.app.sign_in.verify_sign_in()
    print('Test case Passed')

@when('Click on Target terms and conditions link')
def click_terms_conditions(context):
    context.app.sign_in.click_terms_conditions()


@when('Switch to the newly opened window')
def switch_new_window(context):
    # context.app.sign_in.switch_new_window()
    sleep(3)
    all_windows = context.driver.window_handles
    print(f'All window: ', all_windows)
    context.driver.switch_to.window(all_windows[1])
    print('After switched', context.app.sign_in.get_current_window())


@then('Verify Terms and Conditions page is opened')
def verify_term_condition(context):
    context.term_condition = context.app.sign_in.verify_term_condition()
    print('Term and Condition: ', context.term_condition)


@then('Close new window')
def close_window(context):
    context.app.sign_in.close_window()


@then('Switch back to original')
def switch_to_original(context):
    context.app.sign_in.switch_to_window_by_id(context.original_window)
    sleep(2)

@then('Verify account is not found')
def verify_account_not_found(context):
    context.app.sign_in.verify_account_not_found()
    sleep(2)
