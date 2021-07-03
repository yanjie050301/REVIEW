"""
 -*- coding: utf-8 -*-
 @File  : driver.py
 @Author: yanjie
 @Date  : 2021/6/15 0015
 @功能描述  :启动APP
 @实现步骤：
    1.配置参数
    2.启动APP
    3.
"""
from UiAutoTest_chao.common.readconfig import ReadConfig
from appium import webdriver
import time
class Driver():
    def __init__(self):
        self.r = ReadConfig()
    def startUp(self):
        desired_caps = {
          "platformName": self.r.readnews("platformName"),
          # "platformVersion": self.r.readvivo("platformVersion"),
          # "deviceName": self.r.readvivo("deviceName"),
          "platformVersion": self.r.readxiaomi9("platformVersion"),
          "deviceName": self.r.readxiaomi9("deviceName"),
          "appPackage": self.r.readnews("appPackage"),
          "appActivity": self.r.readnews("appActivity"),
          "skipServerInstallation": True,
          "noReset": True
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        print("启动成功")
        time.sleep(10)
        return driver
if __name__ == '__main__':
    d = Driver()
    d.startUp()






