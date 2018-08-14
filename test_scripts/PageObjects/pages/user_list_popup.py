__author__ = 'Frederick'
import json
import os
from selenium.webdriver.common.by import By
from PageObjects.pages.locators import Locator


class AddUserPopUp(object):

    """Initialising the modal elements that will be called in other classes"""
    def __init__(self, driver):
        self.driver = driver

        self.fist_name = driver.find_element(By.XPATH, Locator.FIRST_NAME)
        self.last_name = driver.find_element(By.XPATH, Locator.LAST_NAME)
        self.user_name = driver.find_element(By.XPATH, Locator.USER_NAME)
        self.customer = driver.find_element(By.XPATH, Locator.CUSTOMER)
        self.role = driver.find_element(By.XPATH, Locator.ROLE)
        self.email = driver.find_element(By.XPATH, Locator.EMAIL)
        self.cellphone = driver.find_element(By.XPATH, Locator.CELLPHONE)
        self.addUser_modal = driver.find_element(By.XPATH, Locator.ADD_USER_MODAL)
        self.searchBar = driver.find_element(By.XPATH, Locator.SEARCH_BAR)
        self.password = driver.find_element(By.XPATH, Locator.PASSWORD)
        self.save_button = driver.find_element(By.XPATH, Locator.BUTTON_SAVE)
        self.user_modal_heading = Locator.ADD_USER_MODAL_HEADING
        self.user_num = 0
        self.path = os.getcwd()+'/PageObjects/pages/next_username_number.json'
        self.username_text = ""

    """The get and setter methods to access the page elements above"""

    def get_first_name(self):
        return self.fist_name

    def set_first_name(self, name):
        self.fist_name.clear()
        self.fist_name.send_keys(name)

    def get_last_name(self):
        return self.last_name.text

    def set_last_name(self, surname):
        self.last_name.clear()
        self.last_name.send_keys(surname)

    def set_username_text(self, name, last_name):
        self.username_text = name + last_name

    def get_username_text(self):
        return self.username_text

    """This method is used to get the latest unique number for username"""
    def get_user_num(self):
        with open(self.path) as input_file:
            data = json.load(input_file)
            num = data['username']
        return num

    """This stores the unique number used for incrementing usernames"""
    def set_user_num(self):
        next_num = self.get_user_num() + 1
        user = {"username": next_num}
        with open(self.path, 'w') as output_file:
            json.dump(user, output_file)

    """This method sets a unique username"""
    def set_username(self, first_name, last_name):
        self.set_username_text(first_name, last_name)
        self.set_user_num()
        name = self.get_username_text() + str(self.get_user_num())
        self.user_name.send_keys(name)

    def set_password(self, password):
        self.password.send_keys(password)

    def get_customer(self):
        return self.customer

    def set_customer(self):
        self.customer.click()

    def set_role(self):
        self.role.click()

    def set_email(self, email):
        self.email.send_keys(email)

    def set_cellphone(self, cell_number):
        self.cellphone.send_keys(cell_number)

    def save_user_modal(self):
        self.save_button.click()

    def get_add_user_modal(self):
        return self.addUser_modal

    def get_search_bar(self):
        return self.searchBar

    def get_user_modal_heading(self):
        return self.user_modal_heading

    """Ensures that the form is completed with the details supplied in the parameter"""
    def complete_form(self, details):
        self.set_first_name(details[0])
        self.set_last_name(details[1])
        self.set_username(details[0], details[1])
        self.set_password(details[2])
        self.set_customer()
        self.set_role()
        self.set_email(details[3])
        self.set_cellphone(details[4])
