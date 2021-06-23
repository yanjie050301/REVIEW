"""
 -*- coding: utf-8 -*-
 @File  : basePage.py
 @Author: yanjie
 @Date  : 2021/6/22 0022
 @功能描述  :定义公共的basepage类，对appium提供的部分方法进行二次封装
 @实现步骤：
    1.定义类
    2.定义公共方法
    3.
"""
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage():
    #初始化driver
    def __init__(self,driver):
        self.driver = driver
    #定义公共的方法
    def by_find_element(self,*item):
        #1、强制等待
        # time.sheep(5)
        #2、隐式等待,最多等待5s，如果页面元素在5s内渲染完成，剩下的时间则不等待
        # self.driver.implicitly_wait(5)
        #3、显示等待，每隔时间段查找某个元素，最多等待10s，元素一但查找到则不等待
        try:
            element = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(item))
            return element
        except Exception as msg:
            print(msg)






