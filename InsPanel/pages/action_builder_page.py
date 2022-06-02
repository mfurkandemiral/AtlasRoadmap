import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ActionBuilderPage(BasePage):
    TEMPLATE_LIST = (By.CLASS_NAME, 'template-list')
    SELECT_BUTTON = (By.XPATH, '//*[@class="template-list"]//*[text()="Instory"]/..//*[@class="btn-select"]')
    PASSWORD_TEXT_BOX = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    OK_BUTTON = (By.LINK_TEXT, 'OK')
    TOP_HEADER = (By.CLASS_NAME, 'top-header')
    IFRAME_EDIT = (By.ID, 'iframe-edit')
    VARIATION_LOADING = (By.CSS_SELECTOR, '.loadingWrapper[style="display: none;"]')
    BEFORE_ELEMENT = (By.CLASS_NAME, 'append-before')
    SAVE_BUTTON = (By.CLASS_NAME, 'btn-save')

    def select_instory_template(self):
        self.wait_for_element_visible(self.TEMPLATE_LIST)
        self.find_element(*self.SELECT_BUTTON).click()

    def click_ok_button(self):
        self.click(*self.OK_BUTTON)

    def click_insert_before_element(self):
        with self.switch_frame(self.IFRAME_EDIT):
            self.wait_for_element_clickable(self.TOP_HEADER).click()
        self.wait_for_element_clickable(self.BEFORE_ELEMENT).click()

    def click_save_button(self):
        time.sleep(5)
        self.wait_for_element_clickable(self.SAVE_BUTTON).click()