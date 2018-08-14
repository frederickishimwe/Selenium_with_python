__author__ = 'Frederick'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from PageObjects.pages.locators import Locator
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class WebTablePage(object):

    """Initialisation for page elements that is called from other classes"""
    def __init__(self, driver):
        self.driver = driver

        self.fist_name = driver.find_element(By.XPATH, Locator.TABLE_FIRST_NAME)
        self.last_name = driver.find_element(By.XPATH, Locator.TABLE_LAST_NAME)
        self.user_name = driver.find_element(By.XPATH, Locator.USER_NAME_ON_LIST)
        self.customer = driver.find_element(By.XPATH, Locator.TABLE_CUSTOMER)

        self.deleteButton = driver.find_element(By.XPATH, Locator.TABLE_DELETE_USER)
        self.addUser_button = driver.find_element(By.XPATH, Locator.ADD_USER_BUTTON)
        self.searchBar = driver.find_element(By.XPATH, Locator.SEARCH_BAR)

    """The getter and setter methods used to access the page elements"""
    def get_first_name(self):
        return self.fist_name

    def get_last_name(self):
        return self.last_name

    def get_username(self):
        return self.user_name

    def get_customer(self):
        return self.customer

    def get_add_user_button(self):
        return self.addUser_button

    def get_search_bar(self):
        return self.searchBar

    def get_delete_button(self):
        return self.deleteButton

    """This ensures that no stale elements is thrown by waiting for elements to be present"""
    def wait_for_element(self, locator):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        your_element = WebDriverWait(self.driver, 40, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator)))
        # print('your_element = ', your_element.text, 'is found and present')
        return your_element
