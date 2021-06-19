from androguard.core.bytecodes.apk import APK
from appium import webdriver
import time
a = APK("D:\\appium\\jinritoutiao.apk",False,"r")
package = a.get_package()
activity = a.get_main_activity()

desired_caps = {
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "MI 9",
  "appPackage": package,
  "appActivity": activity,
  "app": "D:\\appium\\jinritoutiao.apk",
  "noReset": True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.quit()