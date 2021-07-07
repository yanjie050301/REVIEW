"""
 -*- coding: utf-8 -*-
 @File  : MyTest.py
 @Author: yanjie
 @Date  : 2021/7/7 0007
 @功能描述  :二次封装unittest方法,继承unittest.testcase方法，初始化setupclass
 @实现步骤：
    1.
    2.
    3.
"""
import unittest
from seleniumUI.common.Log import l
from seleniumUI.common.BaseDriver import Startup
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        l.info("测试环境准备开始")
        cls.driver = Startup()
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        l.info("测试环境准备结束")
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



