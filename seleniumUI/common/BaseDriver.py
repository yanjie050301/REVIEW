"""
 -*- coding: utf-8 -*-
 @File  : BaseDriver.py
 @Author: yanjie
 @Date  : 2021/7/5 0005
 @功能描述  :初始化webdriver，添加是否有无界面运行浏览器
 @实现步骤：
    1.导包
    2.根据是否有无界面进行对应的driver的配置
    3.返回driver
"""
from selenium import webdriver
from seleniumUI.common.ReadConfig import ReadConfig
from seleniumUI.common.ReadConfig import ReadConfig
import time
rc = ReadConfig()
def Startup():
    """
   初始化driver， 并打开百度网址
    :return: 返回driver对象
    """
    driver = webdriver.Chrome()
    url = rc.geturl("url")
    driver.get(url)
    return driver
if __name__ == '__main__':
    d = Startup()
    time.sleep(3)
    d.quit()





