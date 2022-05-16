from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.list_page import ListPage


class ProductPage(BasePage):
    ADD_TO_WISH_LIST_BUTTON = (By.ID, 'add-to-wishlist-button')
    SELECT_LIST = (By.ID, 'atwl-list-name-JTT1GREQ937H')
    VIEW_YOUR_LIST_BUTTON = (By.LINK_TEXT, 'View Your List')

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_wish_list(self):
        self.click(*self.ADD_TO_WISH_LIST_BUTTON)
        self.click(*self.SELECT_LIST)
        self.click(*self.VIEW_YOUR_LIST_BUTTON)
        return ListPage(self.driver)