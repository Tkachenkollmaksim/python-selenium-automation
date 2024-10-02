from behave import given, when, then


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@given('Store original window')
def store_window(context):
    context.orginal_window = context.driver.current_window_handle
    print('Original window: ', context.orginal_window)