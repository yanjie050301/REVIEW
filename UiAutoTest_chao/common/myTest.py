"""
 -*- coding: utf-8 -*-
 @File  : myTest.py
 @Author: yanjie
 @Date  : 2021/6/15 0015
 @功能描述  :继承unittest.TestCase,提前定义setupclass类方法，将driver启动封装到该类中，让testcase子类继承，降低代码重复,避免每条用例都要启动一遍APP
 @实现步骤：
    1.导包unittest
    2.继承unittest.testcase
    3.封装setupclass类方法
"""
from UiAutoTest_chao.common.driver import Driver
from UiAutoTest_chao.common.log import logger
import unittest
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:   #-> None代表这个函数没有返回值
        logger.debug("开始调用Driver类获取APPdriver对象")
        d = Driver()
        cls.driver = d.startUp()
    def setUp(self)-> None:
        pass
    def test(self):
        self.assertEqual(1,1)
    def tearDown(self)-> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        logger.debug("用例执行完毕，关闭该driver")
        cls.driver.quit()
# unittest.main
if __name__ == '__main__':
    unittest.main()




