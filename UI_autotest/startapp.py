"""
功能说明：
1.使用appium启动APP
2.登录APP
3.发布微头条
"""
from appium import webdriver
from androguard.core.bytecodes.apk import APK
import time
# 获取apk的包名和activity
"""
a = APK("F:\\test\\selenium\\app-simulation_-CFAE_-debug.apk",False,"r")
print(a.get_package())
print(a.get_main_activity())
"""

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
  "skipServerInstallation": True,
  "noReset": True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
"""
#同意用户协议
driver.find_element_by_id("com.lchr.diaoyu:id/stv_agree").click()
time.sleep(2)
#获取权限
driver.find_element_by_id("com.lchr.diaoyu:id/rtv_open").click()
time.sleep(2)
#获取电话权限
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(2)
#获取存储权限
driver.find_element_by_id("com.lchr.diaoyu:id/rtv_open").click()
time.sleep(2)
#获取位置权限
driver.find_element_by_id("com.lchr.diaoyu:id/rtv_open").click()
time.sleep(2)
"""
#点击我的icon
driver.find_element_by_id("com.lchr.diaoyu:id/btn_tab_mine").click()
time.sleep(2)
#点击登录
driver.find_element_by_id("com.lchr.diaoyu:id/tv_click2login").click()
time.sleep(2)
#点击密码登录
driver.find_element_by_id("com.lchr.diaoyu:id/login_by_pwd").click()
time.sleep(2)
#输入手机号
driver.find_element_by_id("com.lchr.diaoyu:id/et_account").send_keys(18911032248)
time.sleep(2)
#输入密码
driver.find_element_by_id("com.lchr.diaoyu:id/et_pwd").send_keys("123456789a")
time.sleep(2)
#勾选登录协议
# driver.find_element_by_("com.lchr.diaoyu:id/cb_agree_privacy").click()
time.sleep(10)
#点击登录按钮
driver.find_element_by_id("com.lchr.diaoyu:id/btn_login").click()
time.sleep(10)

driver.quit()
















