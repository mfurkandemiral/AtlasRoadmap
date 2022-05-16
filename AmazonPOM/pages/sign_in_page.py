import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_TEXTBOX = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    PASSWORD_TEXTBOX = (By.ID, 'ap_password')
    SIGN_IN_BUTTON = (By.ID, 'signInSubmit')

    email = "bodixa6881@angeleslid.com"
    password = "Sup3rPassw0rd1"
    skip_text = "skip"

    def __init__(self, driver):
        super().__init__(driver)

    def fill_email_text_box(self):
        self.fill(self.email, *self.EMAIL_TEXTBOX)
        self.click_continue_button()

    def click_continue_button(self):
        self.click(*self.CONTINUE_BUTTON)

    def fill_password_text_box(self):
        time.sleep(3)  # Think time for skip the security step
        self.fill(self.password, *self.PASSWORD_TEXTBOX)
        self.click_sign_in_button()

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)