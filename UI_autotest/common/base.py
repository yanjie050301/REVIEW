"""
功能介绍：让测试用例继承Base类,实现driver活其他类的初始化操作
实现步骤：
1.导入unittest
2.导入driver类
3.在类的初始化方法中创建driver实例并获得driver对象供他人使用
4.在测试用例的初始化方法中，每次用例执行前调用launch_app，使用例执行环境恢复执行前状态
5.在teardownclass方法中，调用quit方法做用例执行完后的清理工作，整个app应用退出
"""
from UI_autotest.common.driver import Driver
from UI_autotest.po.pages.login_page import LoginPage
import unittest

class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试环境开始")
        cls.driver = Driver().start_session()  #初始化driver
        cls.lp = LoginPage(cls.driver)
    def setUp(self):
        print("测试用例开始")
        self.driver.launch_app()   #启动APP，结束一条用例后，环境恢复执行前状态


    def tearDown(self):
        print("测试用例结束")
        self.driver.close_app()    #关闭app,切换到后台，还在内存里
    @classmethod
    def tearDownClass(cls):
        print("测试环境结束")
        cls.driver.quit()     #整体退出，不在内存里