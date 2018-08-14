__author__ = 'Frederick'

import os
import datetime
import unittest
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    """This will be used to calculate duration"""
    started_time = datetime.datetime.now()

    """Setup contains the browser setup attributes"""
    def setUp(self):
        path_ = os.getcwd() + '/../webdriver/chromedriver'
        print(path_)
        self.driver = webdriver.Chrome(path_)
        self.started_time = datetime.datetime.now()
        print('Run Started  : ' + str(self.started_time))
        print('Chrome Environment Setup\n----------------------------')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    """TearDown method closes all the browser instances and then quits"""
    def tearDown(self):
        if not (self.driver is None):
            print('-----------------------------------------------')
            print('\nDestroying Environment  . . . . . .')
            print('End time : '+str(datetime.datetime.now())+'\t Duration :' +
                  str(datetime.datetime.now()-self.started_time))
            self.driver.close()
            self.driver.quit()
