from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestAmazon(BaseTest):
    search_keyword = "samsung"
    pagination_control_text = "2"
    user_name = "Test123"

    def test_amazon(self):
        home_page = HomePage(self.driver)

        self.logger.info("1. Go to Amazon homepage and assert it.")
        self.assertTrue(home_page.is_home_page_opened(), "Home Page is not opened!")
        home_page.dont_change_button_click()
        self.logger.info("Amazon homepage opened successfully.")

        self.logger.info("2. Go to Sign in page and sign in.")
        sign_in_page = home_page.go_to_sign_in_page()
        sign_in_page.fill_email_text_box()
        sign_in_page.fill_password_text_box()
        self.assertEqual(self.user_name, home_page.get_logged_user_name(), "User name doesn't mached!")
        self.logger.info("User has successfuly logged.")

        self.logger.info("3. Search 'samsung' and assert it.")
        search_page = home_page.search_keyword_on_searchbox(self.search_keyword)
        self.assertIn(self.search_keyword, search_page.get_search_keyword_result(), "Search keyword doesn't match!")
        self.logger.info("Search keyword successfuly checked")

        self.logger.info("4. Go to second page and assert it.")
        search_page.go_to_second_page()
        self.assertEqual(self.pagination_control_text, search_page.get_pagination_text(), "Wrong page!")
        self.logger.info("Second page successfully opened.")

        self.logger.info("5. Go to product page and list it.")
        product_page = search_page.select_third_product()
        list_page = product_page.add_to_wish_list()
        self.assertEqual(search_page.get_selected_product_name(), list_page.get_listed_product_name())
        self.logger.info("Product successfully listed.")

        self.logger.info("6. Delete listed product and assert it.")
        list_page.delete_listed_product()
        self.assertTrue(list_page.is_present_undo_text(), "Product could not be deleted from list")
        self.logger.info("Product successfully deleted.")