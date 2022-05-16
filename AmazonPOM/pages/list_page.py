from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ListPage(BasePage):
    LISTED_PRODUCT_NAME = (By.TAG_NAME, 'h2')
    DELETE_BUTTON = (By.NAME, 'submit.deleteItem')
    UNDO_TEXT = (By.ID, 'undo-delete')

    def __init__(self, driver):
        super().__init__(driver)

    def get_listed_product_name(self):
        return self.find_element(*self.LISTED_PRODUCT_NAME).text

    def delete_listed_product(self):
        self.click(*self.DELETE_BUTTON)

    def is_present_undo_text(self):
        return self.find_element(*self.UNDO_TEXT)