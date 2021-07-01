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
from UiAutoTest_chao.PO.MyPage import MyPage
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
        hp = HomePage(self.driver)
        mp = MyPage(self.driver)
        old = int(mp.get_message_text())     #获取发布微头条前头条的数量
        print(f"发布微头条前头条的数量{old}")
        hp.clickFristBatton()    #点击首页按钮
        hp.publish_article(data)#发布微头条
        new = int(mp.get_message_text())     #获取发布成功后微头条数量
        print(f"发布微头条hou头条的数量{new}")
        self.assertEquals(new,old+1)
    """
    def test_samll_message_min(self):
        self.assertEquals(1, 1)
    def test_samll_message_max(self):
        self.assertEquals(1, 1)
    def test_samll_message_null(self):
        self.assertEquals(1, 1)
    """
if __name__ == '__main__':
    unittest.main()

