__author__ = 'Frederick'


class Locator(object):

    """Table elements"""
    SEARCH_BAR = "//input[@type='text'][@placeholder='Search']"
    TABLE_FIRST_NAME = "//*/tr[@ng-repeat='dataRow in displayedCollection']/td[1]"
    TABLE_LAST_NAME = "//*/tr[@ng-repeat='dataRow in displayedCollection']/td[2]"
    USER_NAME_ON_LIST = "//*/tr[@ng-repeat='dataRow in displayedCollection']/td[3]"
    TABLE_CUSTOMER = "//*/tr[@ng-repeat='dataRow in displayedCollection']/td[4]"
    TABLE_DELETE_USER = "//button[@ng-click='delUser()']"

    """ Modal Elements"""
    FIRST_NAME = "//input[@type='text'][@name='FirstName']"
    LAST_NAME = "//input[@type='text'][@name='LastName']"
    USER_NAME = "//input[@type='text'][@name='UserName']"
    PASSWORD = "//input[@type='password'][@name='Password']"
    CUSTOMER = "//*/tr/td/label/input[@value='15']"
    ROLE = "//select[@name='RoleId']/option[text()='Admin']"
    EMAIL = "//input[@type='email']"
    CELLPHONE = "//input[@type='text'][@name='Mobilephone']"
    BUTTON_SAVE = "//Button[.='Save']"

    """Page buttons and search fields"""
    ADD_USER_BUTTON = "//button[@ng-click='pop()'][@type='add']"
    ADD_USER_MODAL = "//*[@class='modal-header']/h3"
    ADD_USER_MODAL_HEADING = 'Add User'
    URL ='http://www.way2automation.com/angularjs-protractor/webtables'
    TITLE = 'Protractor practice website - WebTables'