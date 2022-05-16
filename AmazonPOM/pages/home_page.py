from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.search_page import SearchPage
from pages.sign_in_page import SignInPage


class HomePage(BasePage):
    DONT_CHANGE_BUTTON = (By.CLASS_NAME, "a-button-inner")
    SIGN_IN_BUTTON = (By.ID, "nav-link-accountList")
    MAIN_LOGO = (By.ID, 'nav-logo-sprites')
    SEARCH_TEXTBOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    USER_NAME_TEXT = (By.CLASS_NAME, 'nav-line-1-container')

    def __init__(self, driver):
        super().__init__(driver)

    def is_home_page_opened(self):
        return self.find_element(*self.MAIN_LOGO)

    def dont_change_button_click(self):
        self.find_elements(1, *self.DONT_CHANGE_BUTTON).click()

    def go_to_sign_in_page(self):
        self.click(*self.SIGN_IN_BUTTON)
        return SignInPage(self.driver)

    def search_keyword_on_searchbox(self, search_keyword):
        self.fill(search_keyword, *self.SEARCH_TEXTBOX)
        self.click_search_button()
        return SearchPage(self.driver)

    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)

    def get_logged_user_name(self):
        return self.find_element(*self.USER_NAME_TEXT).text.split(', ')[1]