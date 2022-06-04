from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestCheckWebInstoryCampaign(BaseTest):
    """

    1. Log in the panel, select Optimize and go to Desktop Web Instory
    2. Create Web Instory campaign
    3. Fill all steps till Launch step
    4. Change campaign language, date&time, display settings, add priority and notes
    5. Go to do list and check campaign status is Test and is present in Test link menu
    6. Open campaign's details and check all information that was filled during launch is present there
    7. Go to website with the test link of the campaign
    8. Verify that campaign is visible in storage and class existence contro

    """

    email = "your@mail.com"
    password = "yourpassword"
    condition = "Page Type"
    operator = "is"
    language = "All Languages"
    page_condition = "All Pages"
    activation_time = "Never Ends"
    activation_status = "Test"
    selected_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    priority = "10"
    note = "This campaign was created for Atlas Roadmap."
    campaign_status = "Visible"

    def test_check_web_instory_campaign(self):
        """Test checks completes all steps to create Web Instory campaign and verifies has been created on api side."""
        self.logger.info("1. Log in the panel, select Optimize and go to Desktop Web Instory")
        login_page = LoginPage(self.driver)
        login_page.fill_login_form(self.email, self.password)
        partner_page = login_page.click_login_button()
        self.logger.info("User logged in successfully!")

        self.logger.info("2. Create Web Instory campaign")
        campaign_name = partner_page.generate_campaign_name()
        instory_page = partner_page.select_experience_on_side_menu()
        instory_page.create_desktop_campaign(campaign_name)
        self.logger.info("Web Instory campaign created successfully!")

        self.logger.info("3. Fill all steps till Launch step")
        rules_page = instory_page.add_rule_to_campaign()
        rules_page.select_condition(self.condition).select_operator(self.operator)
        design_pages = rules_page.click_save_and_continue()
        action_builder_page = design_pages.click_add_new_variant()
        action_builder_page.select_instory_template()
        action_builder_page.click_ok_button()
        action_builder_page.click_insert_before_element()
        action_builder_page.click_save_button()
        goals_tab = design_pages.click_save_and_continue()
        launch_tab = goals_tab.click_save_and_continue()
        self.logger.info("Filled all step till launch step successfully!")

        self.logger.info("4. Change campaign language, date&time, display settings, add priority and notes")
        launch_tab.select_personalization_language(self.language)
        launch_tab.change_activation_time(self.activation_time)
        launch_tab.change_display_settings(*self.selected_days)
        launch_tab.change_priority(self.priority)
        launch_tab.change_activation_status(self.activation_status)
        launch_tab.add_note(self.note)
        launch_tab.launch_campaign()
        instory_page.search_campaign(campaign_name)
        instory_page.generate_campaign()
        self.logger.info("Changed campaign language, date&time, display settings, add priority and notes successfully!")

        self.logger.info("5. Go to do list and check campaign status is Test and is present in Test link menu")
        self.assertEqual("Test", instory_page.get_campaign_status(), "Campaign status isn't as expected.")
        self.assertTrue(instory_page.test_link_is_present())
        self.logger.info("Campaign test link and status checked successfully!")

        self.logger.info("6. Open campaign's details and check "
                         "all information that was filled during launch is present there")
        details_page = instory_page.go_to_campaign_details()
        camp_id = details_page.get_campaign_id()
        self.assertEqual(campaign_name, details_page.get_campaign_name(), "Campaign name isn't as expected.")
        self.assertEqual(self.priority, details_page.get_capaign_priority(), "Campaign priority isn't as expected.")
        self.assertEqual(self.condition + " " + self.operator + " " + self.page_condition,
                         details_page.get_campaign_rules(), "Campaign rules isn't as expected.")
        self.assertEqual(self.note, details_page.get_campaign_note(), "Campaign note isn't as expected.")
        details_page.close_detail_side_menu()
        self.logger.info("Campaign's details checked successfully!")

        self.logger.info("7. Go to website with the test link of the campaign.")
        instory_page.click_test_link()
        campaign_page = instory_page.go_to_test_link()
        self.assertEqual(self.campaign_status, campaign_page.get_campaign_visibility(),
                         "Campaign visibility isn't as expected.")
        self.logger.info("Test link was accessed and the campaign was displayed successfully!")

        self.logger.info("8. Verify that campaign is visible in storage and class existence control")
        self.assertTrue(campaign_page.is_present_campaign_class(camp_id), "Campaign class isn't visible.")
        local_storage = campaign_page.partner_page_campaign_control(camp_id)
        self.assertIn('"step1-displayed":true', local_storage, 'No display template log in local storage!')
        self.logger.info("Campaign is visible in storage and class existence controlled successfully!")

    def tearDown(self):
        self.driver.close()