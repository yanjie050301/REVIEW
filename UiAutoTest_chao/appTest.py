"""

"""
from appium import webdriver
import time
desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "vivo X23",
  "appPackage": "com.ss.android.article.news",
  "appActivity": "com.ss.android.article.news.activity.MainActivity",
  "app": "F:\\test\\selenium\\jinritoutiao.apk",
  "skipServerInstallation": True,
  "noReset": True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print("启动成功")
time.sleep(5)
#点击发布按钮
driver.find_element_by_id("com.ss.android.article.news:id/d10").click()
time.sleep(2)
#点击微头条
driver.find_element_by_id("com.ss.android.article.news:id/eor").click()
time.sleep(5)

driver.quit()