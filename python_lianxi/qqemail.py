"""
 -*- coding: utf-8 -*-
 @File  : qqemail.py
 @Author: yanjie
 @Date  : 2021/9/24 0024
 @功能描述  :
 @实现步骤：
    1.
    2.
    3.
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
time.sleep(3)
driver.switch_to.frame("login_frame")   #切换到登录的iframe
driver.find_element_by_id("u").send_keys("1353037583")    #输入账号
driver.find_element_by_id("p").send_keys("yanjie@050301")  #输入密码
driver.find_element_by_id("login_button").click()    #点击登录按钮
driver.switch_to.default_content()   #退出到登录的iframe
time.sleep(5)
driver.find_element_by_id("composebtn").click()    #点击写信按钮
driver.switch_to.frame("mainFrame")   #切换到编辑邮件的iframe
time.sleep(5)
driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input").send_keys("1353037583@qq.com")   #输入收件人
driver.find_element_by_id("subject").send_keys("yanjie@050301")    #输入主题信息
iframe = driver.find_element_by_xpath("//*[starts-with(@id,'_16324')]")
driver.switch_to.frame(iframe)   #切换到编辑正文的iframe
driver.find_element_by_xpath("/html/body").send_keys("ceshiceshi")     #输入正文信息
driver.switch_to.parent_frame()  #退出到编辑正文的iframe
time.sleep(2)
driver.find_element_by_name("sendbtn").click()     #点击发送按钮
driver.switch_to.default_content()   #退出到编辑邮件的iframe
time.sleep(5)







driver.quit()


