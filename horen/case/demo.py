# coding=utf-8
from selenium import webdriver
import time
import unittest
from utils.config import Config
from utils import log
from utils import random_func

e = Config()
url = e.getInfo("login", "url")
username = e.getInfo("login", "username")
password = e.getInfo("login", "password")
class Demo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Config.DRIVER_PATH)
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id("login").click()
        self.driver.maximize_window()
        time.sleep(1)

    def create_user(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="app"]/section/header/ul/li[5]/div').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/form/div[3]/div/button[2]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div/form/div/div[2]/div[1]/div/div/div/div/input').send_keys(random_func.random_name_en())
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div/form/div/div[2]/div[2]/div/div/div/div/input').send_keys("123456")
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div/form/div/div[2]/div[8]/div/button[1]').click()
            time.sleep(1)
            return True
        except:
            return False
    def test_create_user(self):
        result = self.create_user()
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
