# -*- coding:utf-8 -*-

# 测试功能：传统标注

from config import Config
from time import sleep
import unittest


class Traditional(Config):

    # 传统分配
    def test_traditional_assign(self):

        self.login(Config.username[0], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)
        # 点击任务管理，进入管理员页面
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[1]/div').click()
        sleep(Config.STIME)

        # 点击项目管理，进入项目查看页面
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div/div[1]/div").click()
        sleep(Config.STIME+5)

        # 筛选原始项目
        driver.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select/option[2]").click()
        sleep(Config.STIME+2)
        driver.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select/option[2]").click()
        sleep(Config.STIME+2)
        # 点击项目名称，进入项目详情(选择第一个项目，此数据选择还在考虑中)
        driver.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a").click()
        sleep(Config.STIME)

        # 修改项目收益
        driver.find_element_by_id("budget-edit").click()
        sleep(Config.STIME)
        driver.find_element_by_id("new-budget").clear()
        driver.find_element_by_id("new-budget").send_keys("100")
        sleep(Config.STIME)
        driver.find_element_by_id("budget-save").click()
        sleep(Config.STIME)

        # 滑动滚动条
        # js = "var s=document.documentElement.scrollTop=100000"
        # sleep(Config.STIME)
        # driver.execute_script(js)
        # sleep(Config.STIME)

        # 点击新建子项目
        driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/a/button").click()

        # 填写任务数量，默认为总的任务个数，输入5个
        driver.find_element_by_id("unit-count-input").clear()
        driver.find_element_by_id("unit-count-input").send_keys(Config.TASK_AMOUNT)
        sleep(Config.STIME)
        # 选择标注成员
        driver.find_element_by_xpath("//*[@id='edit-button']").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='group-list']/div[12]/input").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='btn-g2m']").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='group-member-list']/div[2]/input").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='btn-m2s']").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='selected-list']/div/input").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='user-content']/button").click()
        sleep(Config.STIME)

        # 选择检查员//*[@id="edit-button"]//*[@id="checker-selector"]/button
        driver.find_element_by_xpath("//*[@id='checker-selector']/button").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='checker-select-dialog']/div/div/div[3]/div/div[2]/div[2]/div[12]/input").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='checker-select-dialog']/div/div/div[3]/div/div[2]/button").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='checker-select-dialog']/div/div/div[3]/div/div[3]/div[2]/div[3]/input").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='checker-select-dialog']/div/div/div[3]/div/div[3]/button").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='checker-select-dialog']/div/div/div[3]/div/div[4]/div[2]/div/input").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='checker-select-dialog']/div/div/div[3]/button").click()
        sleep(Config.STIME)
        # 点击确认提交按钮
        driver.find_element_by_id("commit").click()
        sleep(Config.STIME)

    # 传统标注
    def test_traditional_edit(self):

        # 标注员标注
        self.login(Config.username[1], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        # 选择标注
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div/div[2]/div").click()
        sleep(Config.STIME)

        # 点击标注，进入传统开始标注
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[1]/div').click()
        sleep(Config.STIME)

        # 点击开始标注
        driver.find_element_by_xpath("//*[@id='subjob-list-body']/table/tbody/tr[4]/td[9]/button")
        sleep(60)






if __name__ == "__main__":
    unittest.main()

