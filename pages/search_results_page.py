from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    HEART_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TOOLTIP = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")



    def hover_favorites(self):
        heart_icon = self.find_element(*self.HEART_ICON)

        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform() #Most people miss this step to perform - error will occur if missed

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        sleep(2)
        self.find_element(*self.SIDE_NAV_PRODUCT_NAME)
        sleep(7)

    def store_product_name(self):
        self.wait_for_element_to_appear(*self.SIDE_NAV_PRODUCT_NAME)
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print(f'Product name: {product_name}')


    def verify_favorites(self):
        self.wait_for_element_to_appear(*self.FAV_TOOLTIP)

    def verify_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert product.lower() in actual_result.lower(), f'Expected {product.lower()}, got actual {actual_result.lower()}'
        self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)

    def verify_results_url(self, product):
        self.verify_partial_url(product)


    def click_add_to_cart_side_bar(self):
        self.click(*self.ADD_TO_CART_BTN_SIDE_NAV)
        sleep(3)