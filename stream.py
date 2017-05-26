# -*- coding:utf-8 -*-

# 测试功能：流式标注

from config import Config
from time import sleep
import unittest


class Stream(Config):

    # 流式分配
    def test_1_stream_assign(self):

        # 登录管理员
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

        # 修改流向为流式标注
        driver.find_element_by_id("jobstream-edit").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='stream-select-area']/div[1]/select").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath("//*[@id='stream-select-area']/div[1]/select/option[2]").click()
        sleep(Config.STIME)
        driver.find_element_by_id("change-jobstream-save").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        sleep(Config.STIME+5)

    def test_2_stream_edit(self):

        # 登录标注员
        self.login(Config.username[1], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        # 点击标注，进入标注员管理页面
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div/div[2]/div").click()
        sleep(Config.STIME)
        # 点击流式标注，进入流式标注任务列表页面
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[5]/div').click()
        sleep(Config.STIME+3)

        # 点击第一个任务的开始标注按钮
        driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[3]/td[9]/a').click()
        sleep(Config.STIME+5)

        # 开始标注
        # 提交
        driver.find_element_by_id("next1").click()
        sleep(Config.STIME)

        # 跳过
        driver.find_element_by_id("skip1").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button').click()
        sleep(Config.STIME)
        driver.find_element_by_id("next1").click()
        sleep(Config.STIME)

        # 重标
        driver.find_element_by_id("clear-data1").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        sleep(Config.STIME)
        driver.find_element_by_id("next1").click()
        sleep(Config.STIME)

    # 流式检查【检查操作有待优化成自动识别检查所有任务，目前只能实现检查部分】
    def test_3_stream_check(self):

        # 登录检查员
        self.login(Config.username[2], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        # 点击检查，进入检查员管理页面
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div').click()
        sleep(Config.STIME)

        # 点击流式检查，进入检查任务列表页面
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[4]/div').click()
        sleep(Config.STIME)

        # 选择第一个任务，点击开始检查按钮
        driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[3]/td[9]/a').click()
        sleep(Config.STIME+2)

        # 开始检查操作
        # 修改-修改
        driver.find_element_by_xpath('//*[@id="opt-area-check"]/div[2]/div[1]/button[2]').click()
        sleep(Config.STIME)
        driver.find_element_by_id("updateData").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button').click()
        sleep(Config.STIME)
        # 通过
        driver.find_element_by_id("next2").click()
        sleep(Config.STIME+2)

        # 修改-跳过
        driver.find_element_by_xpath('//*[@id="opt-area-check"]/div[2]/div[1]/button[2]').click()
        sleep(Config.STIME)
        driver.find_element_by_id("updateSkip").click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button').click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button').click()
        sleep(Config.STIME)
        driver.find_element_by_id("next2").click()
        sleep(Config.STIME + 2)

        # 驳回
        driver.find_element_by_id('reject2').click()
        sleep(Config.STIME)
        driver.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button').click()
        sleep(Config.STIME+2)

    # 流式验收
    def test_4_stream_acceptance(self):

        # 登录发布员/验收员
        self.login(Config.username[0], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        # 点击验收，进入验收管理页面
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div').click()
        sleep(Config.STIME)

        # 点击新增验收（流式），进入验收任务页面
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[6]').click()
        sleep(Config.STIME)

        # 选择第一个任务，点击验收
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[11]/a').click()
        sleep(Config.STIME)
        driver.find_element_by_id('new-review-commit').click()
        sleep(Config.STIME)

        # 通过
        driver.find_element_by_id("approve").click()
        sleep(Config.STIME)
        driver.switch_to_alert().accept()
        sleep(10)


# if __name__ == "__main__":
#     unittest.main()

