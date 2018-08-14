__author__ = 'Frederick'

import os
import datetime


class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    '''This method ensures that screenshots are taken with timestamp '''
    def screen_shot(self):
        path = os.getcwd() + '/../test_evidence/' + str(datetime.datetime.now())+'.png'
        self.driver.get_screenshot_as_file(path)

