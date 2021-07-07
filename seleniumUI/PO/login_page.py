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

class LoginPage(BasePage):
    login_button = (By.LINK_TEXT, "登录")
    username = (By.NAME,"username")
    password = (By.NAME,"password")
    login_submit = (By.XPATH,"/html/body/div[1]/div[3]/div/p[3]/span")
    def __init__(self,driver):
        self.driver = driver
    def login(self):
        """
        登录流程
        :return:
        """
        l.info("登录流程开始")
        self.find_element_wait(*self.login_button).click()
        self.find_element_wait(*self.username).send_keys("yanjie000")
        self.find_element_wait(*self.password).send_keys("123123")
        self.find_element_wait(*self.login_submit).click()
        l.info("登录流程结束")


if __name__ == '__main__':
    from seleniumUI.common.BaseDriver import Startup
    driver = Startup()
    lp = LoginPage(driver)
    lp.login()