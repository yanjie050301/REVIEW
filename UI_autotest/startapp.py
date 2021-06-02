"""
功能说明：
1.使用appium启动APP
2.登录APP
3.发布微头条
"""
from appium import webdriver
import time
# desired_caps = {
#   "platformName": "Android",
#   "platformVersion": "10",
#   "deviceName": "MI 9",
#   "appPackage": "com.lchr.diaoyu",
#   "appActivity": "com.lchr.diaoyu.SplashActivity",
#   "app": "F:\\test\\selenium\\diaoyu_3.4.11_wap_release.apk",
#   "noReset": True
# }
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(5)
# driver.quit()
desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "vivo X23",
  "appPackage": "com.lchr.diaoyu",
  "appActivity": "com.lchr.diaoyu.SplashActivity",
  "app": "F:\\test\\selenium\\diaoyu_3.4.11_wap_release.apk",
  "noReset": True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.quit()