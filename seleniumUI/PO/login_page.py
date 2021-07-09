"""
 -*- coding: utf-8 -*-
 @File  : login_page.py
 @Author: yanjie
 @Date  : 2021/7/6 0006
 @功能描述  :记录登录页面的元素，编写相关的方法
 @实现步骤：
    1.
    2.
    3.
"""
from selenium.webdriver.common.by import By
from seleniumUI.PO.BasePage import BasePage
from seleniumUI.common.Log import l
from selenium.webdriver.common.action_chains import ActionChains
import time
class LoginPage(BasePage):
    login_button = (By.LINK_TEXT, "登录")
    username = (By.NAME,"username")
    password = (By.NAME,"password")
    login_submit = (By.XPATH,"/html/body/div[1]/div[3]/div/p[3]/span")
    login_username = (By.XPATH,"/html/body/div[1]/div[1]/div/div[3]/ul")
    loginout_button = (By.LINK_TEXT,"退出登录")
    login_window_close = (By.XPATH,"/html/body/div[1]/div[3]/h2/b")
    def click_login_button(self):
        """
        点击登录按钮
        :return: None
        """
        l.info("点击登录按钮")
        self.find_element_wait(*self.login_button).click()
    def message_input(self,un,pw):
        """
        填写登录信息和提交登录按钮
        :return:None
        """
        l.info("登录流程开始")
        self.find_element_wait(*self.username).send_keys(un)
        self.find_element_wait(*self.password).send_keys(pw)
        self.find_element_wait(*self.login_submit).click()
        l.info("登录流程结束")
    def login(self,un,pw):
        """
        完整的登录流程
        :param un: 用户名
        :param pw: 密码
        :return: None
        """
        self.click_login_button()
        self.message_input(un,pw)
    def getusernametext(self):
        """
        获取已登录状态的用户昵称
        :return: 用户昵称
        """
        usernametext = self.find_element_wait(*self.login_username).text
        return usernametext
    def username_stay(self):
        """
        登录昵称位置鼠标悬浮
        :return: None
        """
        login_username_stay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/ul")
        ActionChains(self.driver).move_to_element(login_username_stay).perform()
    def login_out(self):
        """
        退出登录流程
        :return: None
        """
        self.username_stay()
        self.find_element_wait(*self.loginout_button).click()
    def close_login_window(self):
        """
        关闭登录弹框
        :return: None
        """
        l.info("关闭登录弹窗")
        self.find_element_wait(*self.login_window_close).click()
        time.sleep(3)
    def clear_input(self):
        """
        清空用户名和密码输入框信息
        :return: None
        """
        self.find_element_wait(*self.username).clear()
        self.find_element_wait(*self.password).clear()
if __name__ == '__main__':
    from seleniumUI.common.BaseDriver import Startup
    driver = Startup()
    lp = LoginPage(driver)
    un = "yanjie000"
    pw = ""
    lp.login(un,pw)

    a = lp.find_all_elements(un)
    print("22222222",a)
    # lp.click_login_button()
    # time.sleep(3)
    # lp.close_login_window()
    # lp.login(un,pw)
    # lp.clear_input()


