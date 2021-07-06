"""
 -*- coding: utf-8 -*-
 @File  : Public.py
 @Author: yanjie
 @Date  : 2021/7/5 0005
 @功能描述  :定义公共方法，框架中使用频率高的代码的集合，例如显示等待，获取文件路径等
 @实现步骤：
    1.
    2.
    3.
"""
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumUI.common.Log import l
class public():
    def getdir(self):
        """
        获取当前文件路径
        :return: 返回当前文件路径
        """
        dir = os.path.dirname(os.path.dirname(__file__))
        return dir
    def find_element_wait(self,driver,*item):
        try:
            element = WebDriverWait(driver,30).until(EC.visibility_of_element_located(item))
            return element
        except Exception as msg:
            l.info(msg)
if __name__ == '__main__':
    from seleniumUI.common.BaseDriver import Startup
    from selenium.webdriver.common.by import By
    driver = Startup()
    p = public()
    item = (By.LINK_TEXT,"登录")
    print(p.find_element_wait(driver,*item))





