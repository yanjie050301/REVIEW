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
from UiAutoTest_chao.common.myTest import MyTest
from UiAutoTest_chao.common.readExcle import ReadExcle
from UiAutoTest_chao.common.public import Public
from UiAutoTest_chao.PO.homePage import HomePage

r = ReadExcle()
class LittleMessageTest(MyTest):
    """
    发布微头条用例--正常发布
    """
    def test_samll_message_normal(self):
        # p = Public(self.driver)
        # p.getsize()
        class_name = self.__class__.__name__    #获取类名
        method_name = self._testMethodName     #获取方法名
        data = int(r.read(class_name,method_name))
        hp = HomePage(self.driver)      #发布微头条
        hp.publish_article(data)
        self.assertEquals(1,1)
    def test_samll_message_min(self):
        self.assertEquals(1, 1)
    def test_samll_message_max(self):
        self.assertEquals(1, 1)
    def test_samll_message_null(self):
        self.assertEquals(1, 1)
if __name__ == '__main__':
    unittest.main()

