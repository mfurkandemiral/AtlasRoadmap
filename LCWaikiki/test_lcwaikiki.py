import unittest
import logging

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLCWaikiki(unittest.TestCase):
    DISMISS_COOKIE_BUTTON = (By.CLASS_NAME, 'cookie__dismiss')
    MAIN_LOGO = (By.CLASS_NAME, 'main-header-logo')
    CATEGORY_PAGE_TEXT = (By.TAG_NAME, 'h1')
    FIRST_PRODUCT_ON_CATEGORY_PAGE = (By.CSS_SELECTOR, '.product-card__title:nth-child(1)')
    ADD_TO_CART_BUTTON = (By.ID, 'pd_add_to_cart')
    GO_TO_CART_BUTTON = (By.LINK_TEXT, 'Sepete Git')
    SELECTED_PRODUCT_NAME = (By.CSS_SELECTOR, '.col-xs-7 > .product-title')
    CART_HEADER = (By.CLASS_NAME, 'cart-header')
    CART_COUNT = (By.CLASS_NAME, 'badge-circle')

    base_url = "https://www.lcwaikiki.com/tr-TR/TR"
    menu_text = "ERKEK"
    category_text = "Tişört"
    product_size = "L"
    product_name = ""
    cart_page_header_text = "Sepetim"
    product_count = "1"
    logger = logging.getLogger()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_url(self):
        return self.driver.current_url

    def check_page_loaded(self):
        return True if self.find_element(*self.MAIN_LOGO) else False

    def dismiss_cookie(self):
        self.find_element(*self.DISMISS_COOKIE_BUTTON).click()

    def hover_menu_with(self, menu_text):
        self.hover(By.LINK_TEXT, '{}'.format(menu_text))

    def click_category_with(self, category_text):
        self.find_element(By.LINK_TEXT, '{}'.format(category_text)).click()

    def category_page_control(self):
        return self.find_element(*self.CATEGORY_PAGE_TEXT).text

    def get_product_name(self):
        return self.find_element(*self.FIRST_PRODUCT_ON_CATEGORY_PAGE).text

    def select_product(self):
        self.find_element(*self.FIRST_PRODUCT_ON_CATEGORY_PAGE).click()

    def get_selected_product_name(self):
        return self.find_element(*self.SELECTED_PRODUCT_NAME).text

    def click_add_to_cart_button(self):
        self.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_cart_count(self):
        return self.find_element(*self.CART_COUNT).text

    def go_to_cart_page(self):
        self.find_element(*self.GO_TO_CART_BUTTON).click()

    def select_size(self, product_size):
        self.find_element(By.XPATH, "//*[@size='{}']".format(product_size)).click()

    def click_main_logo(self):
        self.find_element(*self.MAIN_LOGO).click()

    def is_cart_page_loaded(self):
        return self.find_element(*self.CART_HEADER).text

    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(15)

    def test_my_tests(self):
        self.logger.info("1. Go to LC Waikiki homepage and assert it.")
        self.dismiss_cookie()
        self.assertTrue(self.check_page_loaded(), "The main page could not be loaded!")
        self.logger.info("LC Waikiki homepage opened successfully.")

        self.logger.info("2. Go to category page and assert it.")
        self.hover_menu_with(self.menu_text)
        self.click_category_with(self.category_text)
        self.assertIn(self.category_text, self.category_page_control(), "The category page is not correct!")
        self.logger.info("Category page opened successfully.")

        self.logger.info("3. Go to product page and assert it.")
        self.product_name = self.get_product_name()
        self.select_product()
        self.assertEqual(self.product_name, self.get_selected_product_name(), "The product page is wrong.")
        self.logger.info("Product page opened successfully.")

        self.logger.info("4. Add to cart a product and assert it.")
        self.select_size(self.product_size)
        self.click_add_to_cart_button()
        self.assertEqual(self.product_count, self.get_cart_count(), "The product could not added in cart.")
        self.logger.info("Product added successfully.")

        self.logger.info("5. Go to cart page and assert it.")
        self.go_to_cart_page()
        self.assertIn(self.cart_page_header_text, self.is_cart_page_loaded(), "The cart page could not be opened.")
        self.logger.info("Cart page opened successfully.")

        self.logger.info("6. Back to home page and assert it.")
        self.click_main_logo()
        self.assertEqual(self.base_url, self.get_url(), "The Home Page could not be opened. ")
        self.logger.info("Homepage opened successfully.")

    def tearDown(self):
        self.driver.close()