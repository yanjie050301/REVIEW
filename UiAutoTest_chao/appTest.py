"""

"""


from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
time.sleep(10)
#隐式等待
# driver.implicitly_wait(5)
#显示等待：最长等待10s，每0.5s检查一次页面是否有该元素,有的话停止等待
# items = (By.ID,"com.ss.android.article.news:id/d10")
# WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(items))
# print("已发现发布按钮")
#获得当前页面所有元素
# page = driver.page_source
#
# if str(page).find("发布")==1:
#   print("当前页面已找到发布按钮")
# size = public.getsize(driver)
# print(size)
# public.swipeup(driver)
# print("向上滑动")
#点击发布按钮
# driver.find_element(By.ID,"com.ss.android.article.news:id/d10").click()
driver.find_element_by_id("com.ss.android.article.news:id/d28").click()

time.sleep(2)
# #点击微头条
# driver.find_element_by_id("com.ss.android.article.news:id/eor").click()
# time.sleep(5)
# #输入内容
# driver.find_element_by_id("com.ss.android.article.news:id/an5").send_keys("123456")
# time.sleep(5)
# #点击发布按钮
# driver.find_element_by_id("com.ss.android.article.news:id/dxl").click()
# time.sleep(5)

driver.quit()

























