"""
 -*- coding: utf-8 -*-
 @File  : HomeTest.py
 @Author: yanjie
 @Date  : 2021/6/15 0015
 @功能描述  :封装testcase
 @实现步骤：
    1.
    2.
    3.
"""

import unittest,time
from selenium.webdriver.common.by import By
from UiAutoTest_chao.common.driver import Driver
from UiAutoTest_chao.common.myTest import MyTest
from UiAutoTest_chao.common.readExcle import ReadExcle
from UiAutoTest_chao.common.public import Public
r = ReadExcle()
class LittleMessageTest(MyTest):
    """
    发布微头条用例
    """
    def test_samll_message_normal(self):
        p = Public(self.driver)
        p.getsize()
        class_name = self.__class__.__name__    #获取类名
        method_name = self._testMethodName     #获取方法名
        # print("class_name:",class_name)
        # print("method_name:",method_name)
        data = r.read(class_name,method_name)
        # d = Driver()
        # driver = d.startUp()
        # # 点击发布按钮
        # self.driver.find_element_by_id("com.ss.android.article.news:id/d10").click()
        # time.sleep(2)
        # # # 点击微头条
        # self.driver.find_element_by_id("com.ss.android.article.news:id/eor").click()
        # time.sleep(5)
        # # # 输入内容
        # self.driver.find_element_by_id("com.ss.android.article.news:id/an5").send_keys(data)
        # time.sleep(5)
        # # # 点击发布按钮
        # self.driver.find_element_by_id("com.ss.android.article.news:id/dxl").click()
        # time.sleep(5)

        self.assertEquals(1,1)
    def test_samll_message_min(self):
        self.assertEquals(1, 1)
    def test_samll_message_max(self):
        self.assertEquals(1, 1)
    def test_samll_message_null(self):
        self.assertEquals(1, 1)
if __name__ == '__main__':
    unittest.main()

