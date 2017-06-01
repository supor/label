# -*- coding:utf-8 -*-

# 测试功能：流式标注

from config import Config
from time import sleep
import unittest


class Stream(Config):
    print """
        流式分配"""

    def est_1_stream_assign(self):

        print("管理员登录")
        self.login(Config.username[0], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        print '进入管理员页面'
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[1]/div')

        print "进入项目列表页面"
        self.find_element_by_xpath("//*[@id='main']/div/div[2]/div/div[1]/div")

        print "筛选已导入的第一个项目"
        self.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select")
        self.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select/option[2]")
        self.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select")
        self.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select/option[2]")
        print "进入第一个项目详情页面"
        self.find_element_by_xpath("//*[@id='root']/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a")

        print "修改流向为流式标注"
        self.find_element_by_id("jobstream-edit")
        sleep(Config.STIME+2)
        self.find_element_by_xpath("//*[@id='stream-select-area']/div[1]/select")
        self.find_element_by_xpath("//*[@id='stream-select-area']/div[1]/select/option[2]")
        self.find_element_by_id("change-jobstream-save")
        self.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]')
        sleep(Config.STIME+2)

    def est_2_stream_edit(self):
        print """
标注员标注流程
            """
        print "标注员登录"
        self.login(Config.username[1], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        print "点击标注，进入标注员管理页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[5]/div')
        print "点击流式标注，进入流式标注任务列表页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[5]/div')

        print "点击第一个任务的开始标注按钮"
        self.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[5]/td[8]')

        print """
        开始标注...
        """
        print "提交"
        self.find_element_by_id("next1")

        print "跳过"
        self.find_element_by_id("skip1")
        self.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button')
        self.find_element_by_id("next1")

        print "重标"
        self.find_element_by_id("clear-data1")
        self.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]')
        self.find_element_by_id("next1")

    # 【检查操作有待优化成自动识别检查所有任务，目前只能实现检查部分】
    def est_3_stream_check(self):
        print """
        流式检查
        """
        print "检查员登录"
        self.login(Config.username[2], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        print "点击检查，进入检查员管理页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div')

        print "点击流式检查，进入检查任务列表页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[4]/div')
        sleep(Config.STIME)

        print "选择第一个任务，点击开始检查按钮"
        self.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[3]/td[9]/a')
        sleep(Config.STIME+2)

        print """
        开始检查操作...
        """
        print "修改-修改"
        self.find_element_by_xpath('//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
        self.find_element_by_id("updateData")
        self.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button')

        print "通过"
        self.find_element_by_id("next2")
        sleep(Config.STIME+2)

        print "修改-跳过"
        self.find_element_by_xpath('//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
        self.find_element_by_id("updateSkip")
        self.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button')
        self.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button')
        self.find_element_by_id("next2")
        sleep(Config.STIME + 2)

        print "驳回"
        self.find_element_by_id('reject2')
        self.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button')
        sleep(Config.STIME+2)

    def est_4_stream_acceptance(self):
        print """
            流式验收
            """
        print "登录发布员/验收员"
        self.login(Config.username[0], Config.pwd)
        driver = self.driver
        sleep(Config.STIME)

        print "点击验收，进入验收管理页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div')

        print "点击新增验收（流式），进入验收任务页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[6]')

        print "选择第一个任务，点击验收"
        self.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[11]/a')
        self.find_element_by_id('new-review-commit')

        print "放弃"
        self.find_element_by_id("reject")

        self.find_element_by_id("reason-btn")
        sleep(Config.STIME+2)

        print """
        批驳
        """
        print "返回首页"
        self.find_element_by_xpath('//*[@id="navbar"]/div[2]/ul/li[1]/a')
        print "点击任务管理，进入管理员页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[1]/div')
        print "点击批驳验收，进入批驳列表"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div')
        print "批驳按钮，进入批驳页面"
        self.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[12]/a')
        print "反对驳回"
        self.find_element_by_id('reject')
        self.find_element_by_id('reason-btn')
        self.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
        sleep(Config.STIME+2)

        print """
        进入管理批驳页面
        """
        print "返回首页"
        self.find_element_by_xpath('//*[@id="navbar"]/div[2]/ul/li[1]')
        print "点击验收，进入验收管理页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div')
        print "进入管理批驳（流式）页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[5]/div')

        print """
        筛选出项目类型 （假脸识别）
        """
        self.find_element_by_xpath('//*[@id="condition-area"]/select[1]')
        self.find_element_by_xpath('//*[@id="condition-area"]/select[1]/option[10]')

        print "筛选出验收中的数据"
        print "选择验收"
        self.find_element_by_xpath('//*[@id="condition-area"]/select[2]')
        self.find_element_by_xpath('//*[@id="condition-area"]/select[2]/option[2]')
        print "点击提交"
        self.find_element_by_xpath('//*[@id="condition-area"]/button')

        print "放弃验收"
        print "选择第一条数据，点击继续验收"
        self.find_element_by_xpath('//*[@id="subjob-list"]/table/tbody/tr[1]/td[8]/a[1]')
        print "点击放弃"
        self.find_element_by_id('giveup')
        driver.switch_to_alert().accept()
        sleep(Config.STIME+2)

        print """验收通过
        
        """
        print "返回首页"
        self.find_element_by_xpath('//*[@id="navbar"]/div[2]/ul/li[1]/a')
        print "点击验收，进入验收管理页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div')
        print "点击新增验收（流式），进入验收任务页面"
        self.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[6]')
        print "选择第一个任务，点击验收"
        self.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[11]/a')
        self.find_element_by_id('new-review-commit')
        print "点击通过"
        self.find_element_by_id("approve")
        driver.switch_to_alert().accept()
        sleep(Config.STIME)


# if __name__ == "__main__":
#     unittest.main()

