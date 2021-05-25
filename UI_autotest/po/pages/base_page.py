"""
功能介绍：
"""
import time

class BasePage():
    def __init__(self,driver):
        self.driver = driver
    def wait(self,s):
        time.sleep(s)
    def search_element(self,loc,mag=""):
        element =  self.driver.find_element.by(*loc)
        print(f"找到页面元素{msg}")
        return element
    def click_element(self,loc,msg=""):
        self.search_element(loc,msg).click()
        print(f"点击页面元素：{msg}")
    def send_data(self,loc,data,msg = ""):
        self.search_element(loc,msg).sengkeys(data)
        print(f"向页面元素发送数据{msg}")



