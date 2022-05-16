from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):
    SEARCH_KEYWORD_CONTROL_TEXT = (By.CSS_SELECTOR, 'span .a-text-bold')
    SECOND_PAGE_BUTTON = (By.LINK_TEXT, '2')
    PAGINATION_CONTROL_ATTRIBUTE = (By.XPATH, '//span[@aria-label="Current page, page 2"]')
    THIRD_PRODUCT = (By.TAG_NAME, 'h2')

    product = ""

    def __init__(self, driver):
        super().__init__(driver)

    def get_search_keyword_result(self):
        return self.find_element(*self.SEARCH_KEYWORD_CONTROL_TEXT).text

    def go_to_second_page(self):
        self.clickable_element(self.SECOND_PAGE_BUTTON).click()

    def get_pagination_text(self):
        return self.find_element(*self.PAGINATION_CONTROL_ATTRIBUTE).text

    def select_third_product(self):
        self.product = self.driver.find_elements(*self.THIRD_PRODUCT)[2].text
        self.click(By.XPATH, "//span[text()='{}']".format(self.product))
        return ProductPage(self.driver)

    def get_selected_product_name(self):
        return self.product