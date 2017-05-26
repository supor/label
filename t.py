# -*- coding:utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def Transfer_Clicks():
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application/chromedriver")
    browser.get("http://baike.baidu.com/link?url=BOBcwJDcyCH1Ne3_axo3ESSZYloQybkgviDdNkW_chweLoC1wwcTjFWkQKEtUtmbjAPlKVQeSL89CWO81dxq8K")
    sleep(5)
    ActionChains(browser).send_keys(Keys.DOWN).perform()
    sleep(5)

Transfer_Clicks()