"""

"""
from appium import webdriver
import time
desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "vivo X23",
  "appPackage": "com.lchr.diaoyu",
  "appActivity": "com.lchr.diaoyu.SplashActivity",
  "app": "F:\\test\\selenium\\diaoyu_3.4.11_wap_release.apk",
  "skipServerInstallation": True,
  "noReset": True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)