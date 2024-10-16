from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH_PROD = (By.ID, 'search')
    CLICK_SEARCH = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def open_main(self):
        self.open('https://www.target.com/')




