"""
@Time : 2021/6/5 13:45
@Author : 远秋
@Email : gongyuanqiu@163.com
@File : appTest.py
@Project : AppUIAutomation
@feature : 
@实现步骤：
"""

#导包
from appium import webdriver
from selenium.webdriver.common.by import By
import time
import public

#创建app相关参数配置
def startUP():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "MI 9",
        "appPackage": "com.ss.android.article.news",
        "appActivity": "com.ss.android.article.news.activity.MainActivity",
        "app": "D:\\appium\\jinritoutiao.apk",
        "noReset": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    print("启动成功")
    time.sleep(10)
    # public.swipeUp(driver)
    # 点击右上角发布
    # driver.find_element(By.ID,"com.ss.android.article.news:id/bov").click()
    # time.sleep(2)
    # items = driver.find_element(By.CLASS_NAME,"android.widget.ImageView")
    # items[0].click()
    assert 1==2,print("断言失败")
    driver.quit()
#调试
if __name__=="__main__":
    startUP()
