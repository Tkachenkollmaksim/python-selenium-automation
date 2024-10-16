from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.base_page import Page

class SignIn(Page):
    VERIFY_SIGN_IN = (By.CSS_SELECTOR, '.sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs')
    Term_Cond = (By.CSS_SELECTOR, '.sc-676073c3-0.sc-5f0b2968-0.kbivTL.gvPtqx')
    SIGN_IN = (By.CSS_SELECTOR, '.sc-58ad44c0-3.kwbrXj.h-margin-r-x3')
    NAV_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    VERIFY_TERM_COND = (By.CSS_SELECTOR, '.sc-fe064f5c-0.dtCtuk')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SIGNING_IN = (By.CSS_SELECTOR, '.sc-ddc722c0-0.sc-f1230b39-0.sc-ea08e237-4.bsiKgd.doBYzz.bveVWO')
    ACC_NOT_FOUND = (By.CSS_SELECTOR, '.sc-55a9f08c-0.ccRcBB')

    def open_sign_in(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_nav_sign_in(self):
        self.wait_to_be_clickable_click(*self.NAV_SIGN_IN)

    def verify_sign_in(self):
        actual_result = self.driver.find_element(*self.VERIFY_SIGN_IN).text
        expected_result = 'Sign into your Target account'
        assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
        sleep(1)

    def click_terms_conditions(self):
        self.wait_to_be_clickable_click(*self.Term_Cond)

    def verify_term_condition(self):
        self.find_element(*self.VERIFY_TERM_COND)

    def close_window(self):
        self.driver.close()

    # def switch_to_original(self):
    #     self.

    # def verify_terms_conditions_opened(self):
    #     self.verify_partial_url('target-privacy-policy/')

    def incorrect_email(self, text):
        self.input_text(text, *self.USERNAME)
        # self.input_text(*self.USERNAME)
        # self.click(*self.USERNAME)
        sleep(1)

    def incorrect_pass(self, input):
        sleep(1)
        self.input_text(input, *self.PASSWORD)
        # self.click(*self.SIGNING_IN)

    def click_sign_in_button(self):
        self.click(*self.SIGNING_IN)

    def verify_account_not_found(self):
        self.find_element(*self.ACC_NOT_FOUND)
        sleep(2)

