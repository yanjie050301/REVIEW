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

import unittest
from selenium.webdriver.common.by import By
from UiAutoTest_chao.common.driver import Driver
from UiAutoTest_chao.common.myTest import MyTest
class LittleMessageTest(MyTest):
    """
    发布微头条用例
    """
    def test_samll_message_normal(self):
        # d = Driver()
        # driver = d.startUp()
        #点击发布按钮
        # driver.find_element(By.ID,"com.ss.android.article.news:id/d10").click()
        self.assertEquals(1,1)
    def test_samll_message_min(self):
        self.assertEquals(1, 1)
    def test_samll_message_max(self):
        self.assertEquals(1, 1)
    def test_samll_message_null(self):
        self.assertEquals(1, 1)
if __name__ == '__main__':
    unittest.main()

