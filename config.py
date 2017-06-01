# -*- coding:utf-8 -*-
# 整体配置

from selenium import webdriver
from time import sleep
import unittest


class Config(unittest.TestCase):

    STIME = 1
    TASK_AMOUNT = "1"
    # 用户登录名和密码
    username = ["r", "c3", "c4"]
    pwd = "dev"

    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver')
        self.base_url = "http://liyubao.dev.zzcrowd.com/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def find_element_by_xpath(self, xpath, send_keys_text="", handle_type="click"):
        if handle_type is "click":
            self.driver.find_element_by_xpath(xpath).click()
            sleep(Config.STIME)
        else:
            self.driver.find_element_by_xpath(xpath).send_keys(send_keys_text)
            sleep(Config.STIME)

    def find_element_by_id(self, id_xpath, send_keys_text="", handle_type="click"):
        if handle_type is "click":
            self.driver.find_element_by_id(id_xpath).click()
            sleep(Config.STIME)
        else:
            self.driver.find_element_by_id(id_xpath).send_keys(send_keys_text)
            sleep(Config.STIME)

    def login(self, username, passwd):

        # 登录
        self.driver.get(self.base_url)
        sleep(Config.STIME)
        # 点击主页的登录按钮
        self.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[5]/a")
        # 登录定位
        self.find_element_by_id('username', username, "send_keys")
        self.find_element_by_id('password', passwd, "send_keys")
        self.find_element_by_id('submit')

