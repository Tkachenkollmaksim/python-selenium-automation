from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN = (By.CSS_SELECTOR, '.sc-58ad44c0-3.kwbrXj.h-margin-r-x3')
    NAV_SIGN_IN = (By.CSS_SELECTOR, '.sc-859e7637-0.hHZPQy')


    # def sign_in(self):
    #     self.click(*self.SIGN_IN)
    #     sleep(2)

    def nav_sign_in(self):
        self.click(*self.NAV_SIGN_IN)
        sleep(1)


    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(9)

    def click_cart(self):
        #self.wait_to_be_clickable_click(*self.CART_BTN)
        # < selenium.webdriver.remote.webelement.WebElement(session="04bc84233634023eb4c559b5a2d6f046",
        # element="f.13F45D4F93A179BA185F4B4424017BB3.d.D698E4C69D359A83E856BB83A284E425.e.118") >
        cart_btn = self.driver.find_element(*self.CART_BTN)
        print("Before Refresh", cart_btn)

        self.driver.refresh()
        cart_btn = self.driver.find_element(*self.CART_BTN)

        print("After Refresh", cart_btn)
        print(cart_btn)

        cart_btn.click()

