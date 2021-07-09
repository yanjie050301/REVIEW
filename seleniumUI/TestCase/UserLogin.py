"""
 -*- coding: utf-8 -*-
 @File  : UserLogin.py
 @Author: yanjie
 @Date  : 2021/7/7 0007
 @功能描述  :登录流程的测试用例
 @实现步骤：
    1.
    2.
    3.
"""
import unittest
from seleniumUI.common.Log import l
from seleniumUI.PO.login_page import LoginPage
from seleniumUI.common.MyTest import MyTest
from seleniumUI.common.ReadExcle import ReadExcle
class LoginTest(MyTest):
    re = ReadExcle()
    def test_login_normal(self):
        """
        正确用户名密码登录
        :return:
        """
        c = self.__class__.__name__
        m = self._testMethodName
        np = self.re.getvalue(c,m)
        un = np[0]
        pw = int(np[1])
        lp = LoginPage(self.driver)
        lp.login(un,pw)
        final = lp.find_all_elements(un)  #获取页面用户名信息
        lp.login_out()  #退出登录
        self.assertTrue(final == True)
        l.info("第一条用例执行完毕")

    def test_login_uerror(self):
        c = self.__class__.__name__
        m = self._testMethodName
        np = self.re.getvalue(c, m)
        un = np[0]
        pw = int(np[1])
        lp = LoginPage(self.driver)
        lp.login(un,pw)
        final = lp.find_all_elements(un)  #获取页面用户名信息
        lp.close_login_window()  #关闭登录弹框
        self.assertFalse(final)
        l.info("第二条用例执行完毕")

    def test_login_perror(self):
        c = self.__class__.__name__
        m = self._testMethodName
        np = self.re.getvalue(c, m)
        un = np[0]
        pw = int(np[1])
        lp = LoginPage(self.driver)
        lp.click_login_button()  #点击登录按钮
        lp.clear_input()     #清除用户名密码输入框信息
        lp.message_input(un,pw)   #重新输入用户名和密码
        final = lp.find_all_elements(un)  #获取页面用户名信息
        lp.close_login_window()  #关闭登录弹框
        self.assertFalse(final)
        l.info("第三条用例执行完毕")

    def test_login_unull(self):
        c = self.__class__.__name__
        m = self._testMethodName
        np = self.re.getvalue(c, m)
        un = np[0]
        pw = int(np[1])
        lp = LoginPage(self.driver)
        lp.click_login_button() #点击登录按钮
        lp.clear_input() #清除用户名密码输入框信息
        lp.message_input(un, pw)
        final = lp.find_all_elements(un) #获取页面用户名信息
        lp.close_login_window()  #关闭登录弹框
        self.assertFalse(final)
        l.info("第四条用例执行完毕")

    def test_login_pnull(self):
        c = self.__class__.__name__
        m = self._testMethodName
        np = self.re.getvalue(c, m)
        un = np[0]
        pw = int(np[1])
        lp = LoginPage(self.driver)
        lp.click_login_button() #点击登录按钮
        lp.clear_input() #清除用户名密码输入框信息
        lp.message_input(un, pw) #重新输入用户名和密码
        final = lp.find_all_elements(un) #获取页面用户名信息
        lp.close_login_window()  #关闭登录弹框
        self.assertFalse(final)
        l.info("第五条用例执行完毕")

if __name__ == '__main__':
    unittest.main()





