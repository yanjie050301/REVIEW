"""
 -*- coding: utf-8 -*-
 @File  : BasePage.py
 @Author: yanjie
 @Date  : 2021/7/7 0007
 @功能描述  :显示等待方法
 @实现步骤：
    1.
    2.
    3.
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumUI.common.Log import l
from selenium.webdriver.common.action_chains import ActionChains
import time
class BasePage():
    def __init__(self,driver):
        self.driver = driver
    def find_element_wait(self, *item):
        """
        显示等待
        :param item: 查找的元素
        :return: 查找到的原始
        """
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(item))
            return element
        except Exception as msg:
            l.info(msg)
    def action_chains(self,item):
        """
        鼠标悬停
        :param item: 需要停留的元素
        :return: None
        """
        try:
            ActionChains(self.driver).move_to_element(item).perform()
        except Exception as msg:
            l.info(msg)
        else:
            l.info("悬停成功")
    def find_all_elements(self,value):
        """
        添加断言，当页面元素无法定位到的时候，可以使用page_source方法获取页面全部元素，然后在使用find方法进行查找某元素
        :param value: 需要查找的元素
        :return: 找到该元素返回Ture，反之返回False
        """
        time.sleep(3)
        try:
            element = self.driver.page_source
            f = element.find(value)
            if f != -1:
                return True
            else:
                return False
        except Exception as msg:
            l.info(msg)

if __name__ == '__main__':
    from seleniumUI.common.BaseDriver import Startup
    from selenium.webdriver.common.by import By
    driver = Startup()
    item = (By.LINK_TEXT, "登录")
    u = "登录"
    # login_username = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/ul")
    bp = BasePage(driver)
    print(bp.find_all_elements(u))