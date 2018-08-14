__author__ = 'Frederick'

import unittest
from selenium.common.exceptions import StaleElementReferenceException
from test_utility.screenshot import ScreenShot
from PageObjects.pages.user_list_popup import Locator, AddUserPopUp
from PageObjects.pages.webtables import WebTablePage
from test_base.environment_setup import EnvironmentSetup


class TC01AddUserAndSearchFunctionality(EnvironmentSetup):
    """test_and_verify_new_user  navigates to the url and adds a new user to the user list tables
    And then verifies to make sure that, that newly added user exist in the user list table"""
    def test_and_verify_new_user(self):

        """Using the driver instance created in the environment setup"""
        driver = self.driver
        screen_shot = ScreenShot(driver)

        '''Navigate to URL : '''
        self.driver.get(Locator.URL)  # This is a common url, therefore this url is stored in the locator file
        self.driver.set_page_load_timeout(20)
        print('Step 01: Navigate to URL:', Locator.URL)

        try:
            if self.driver.title == Locator.TITLE:  # tile == Protractor practice website - WebTables
                self.assertEqual(driver.title, Locator.TITLE)
                print('Step 02: Validated that user list table has loaded successfully')
            else:
                if WebTablePage.get_search_bar().is_displayed():
                    print('Title does not match  but search bar is displayed')
                    raise StaleElementReferenceException

            """Initialise the user_list_table when page has loaded, to ensure all elements exist before calling them"""
            user_list_table = WebTablePage(self.driver)

            """Ensure the Add User button is loaded before clicking on it"""
            if user_list_table.get_add_user_button().is_displayed():
                user_list_table.get_add_user_button().click()
                self.driver.implicitly_wait(5)
                print('Step 03: Click Add User button')

            """Initialise Modal elements"""
            user_list_pop = AddUserPopUp(self.driver)

            """Ensure  Popup Modal is loaded with the correct modal heading"""
            if user_list_pop.get_add_user_modal().is_displayed():
                modal_heading = user_list_pop.get_add_user_modal().text
                self.assertEqual(modal_heading, user_list_pop.user_modal_heading)  # verify that correct popup is loaded

            """Enter new user when form is displayed on the popup modal"""
            if user_list_pop.get_first_name().is_displayed():
                details = ['Fname', 'Lname', 'password', 'test@email.com', '0000 000 000']
                username = details[0]+details[1]+str(user_list_pop.get_user_num()+1)
                print('Step 04: Add users with the following details : ', details)

                """This statement completes the form with the supplied user details"""
                user_list_pop.complete_form(details)

                self.driver.implicitly_wait(500)

                """Take Screen Shot to ensure that form was completed successfully"""
                screen_shot.screen_shot()
                user_list_pop.save_user_modal()
                self.driver.implicitly_wait(500)
                print('Step 05: Ensure that username ', username, 'is unique')

            """This ensures that when the user list table is displayed, a new username will be searched"""
            if user_list_table.get_search_bar().is_displayed():
                user_list_table.get_search_bar().send_keys(username)
                self.driver.implicitly_wait(900)

                """Take Screen Shot to ensure that newly added user was listed in the user list table"""
                screen_shot.screen_shot()

            """This statement ensures that a searched username exist in the table and is present"""
            if user_list_table.wait_for_element(Locator.USER_NAME_ON_LIST).is_displayed():
                self.assertEqual(user_list_table.wait_for_element(Locator.USER_NAME_ON_LIST).text, username)
                print('Step 06: Ensure that username  = ', username, ' is added to the list')

        except StaleElementReferenceException as e:
            print('Page Object Element is not found or present use the wait_for_element(locator l) '
                  'to wait until present : \n', e.msg)

        except Exception as e:
            print('Error :  Something else went wrong during runtime, please investigate  \n', e.with_traceback())


if __name__ == '__main__':
    unittest.main()

