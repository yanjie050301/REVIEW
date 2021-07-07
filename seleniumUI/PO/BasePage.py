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
class BasePage():
    def __init__(self,driver):
        self.driver = driver
    def find_element_wait(self, *item):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(item))
            return element
        except Exception as msg:
            l.info(msg)
if __name__ == '__main__':
    from seleniumUI.common.BaseDriver import Startup
    from selenium.webdriver.common.by import By
    driver = Startup()
    item = (By.LINK_TEXT, "登录")
    bp = BasePage(driver)
    print(bp.find_element_wait(*item))