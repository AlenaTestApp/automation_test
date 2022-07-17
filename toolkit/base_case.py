import datetime

from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from config.conf_data import *
import time
import sys
print(sys.path)


class BaseCase(unittest.TestCase):

    driver = None
    outcome = None

    # def __init__(self, methodName: str = ...):
    #     super().__init__(methodName)
    #self._outcome = None
    _outcome = None

    @classmethod
    def setUpClass(cls):
        print("=============================setUpClass=========================")
        driver_exe = Service(driver_path)
        cls.driver = webdriver.Chrome(service=driver_exe)
        print("=============================exit_setUpClass====================")

    def setUp(self):
        print("=============================setUP==============================")
        self.driver.get(HOME_PAGE)
        print("=============================exit_setUP=========================")

    def tearDown(self):
        print("=============================tearDown===========================")
        # t = time.gmtime(time.time())
        # ct = ':'.join([str(i) for i in [t.tm_hour, t.tm_min, t.tm_sec]])
        filename = self._testMethodName + "_" + time.strftime("%H-%M-%S") + ".png"
        try:
            for method, error in self._outcome.errors:
                print('Meth, OUT ', method, error)
                if error:
                    #self.driver.save_screenshot(r"screenshots/" + filename)
                    self.driver.get_screenshot_as_file(r"screenshots/" + filename)
                    #self.driver.get_screenshot_as_file(self.id().split('.')[-1] + "_" + ct + ".png")
        except Exception as e:
            print('Error detected ', e)
        print("=============================exit_tearDown======================")

    @classmethod
    def tearDownClass(cls):
        print("=============================tearDownClass======================")
        cls.driver.quit()
        print("=============================exit_tearDownClass=================")
