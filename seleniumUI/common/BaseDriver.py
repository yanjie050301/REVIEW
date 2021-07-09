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
from seleniumUI.common.Log import l
import time
rc = ReadConfig()
def Startup():
    """
   初始化driver， 并打开百度网址
    :return: 返回driver对象
    """
    wui = rc.getgui("gui")
    option = webdriver.ChromeOptions()
    if wui == "yes" or wui == "Yes":
        l.info("浏览器有界面运行")
        """
        保存浏览器登录信息
        """
        option.add_argument(r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
        """
        禁用浏览器记住密码弹窗
        """
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs[
            "profile.password_manager_enabled"] = False
        option.add_experimental_option("prefs", prefs)
        """
               方法针对V78版本及以上有效
               解决Chrome正在受到自动软件的控制的办法
               """
        option.add_experimental_option("useAutomationExtension",False)
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_argument("--start-maximized") #窗口最大化
        driver = webdriver.Chrome(chrome_options=option)
    else:
        l.info("浏览器无界面运行")
        option.add_argument("headless")  # 设置无浏览器界面
        """
                保存浏览器登录信息
                """
        option.add_argument(r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
        """
        禁用浏览器记住密码弹窗
        """
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs[
            "profile.password_manager_enabled"] = False
        option.add_experimental_option("prefs", prefs)
        """
               方法针对V78版本及以上有效
               解决Chrome正在受到自动软件的控制的办法
               """
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--start-maximized")  # 窗口最大化
        driver = webdriver.Chrome(chrome_options=option)
    url = rc.geturl("url")
    driver.get(url)
    l.info(f"成功打开{url}页面")
    return driver
if __name__ == '__main__':
    d = Startup()
    time.sleep(3)
    d.quit()





