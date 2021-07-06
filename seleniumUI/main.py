

import time
from selenium import webdriver
from seleniumUI.common.Public import public
def StartUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://www.wanandroid.com/")
    time.sleep(3)
    """
    t = driver.find_element_by_class_name("alink")
    print("text为：",t.text)
    print("attribute为：",t.get_attribute("namespaceURI"))
    t.click()      
    hendle = driver.window_handles    #获取浏览器所以窗口
    print(hendle)
    driver.switch_to.window(hendle[1])   #切换到浏览器第二个窗口
    driver.get_screenshot_as_file("111.png")   #截图
    time.sleep(3)
    """
    return driver
def register():
    driver = StartUp()
    driver.find_element_by_link_text("注册").click()
    item = "yanjie123"
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/input[1]").send_keys(item)
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("123456789")
    time.sleep(2)
    driver.find_element_by_name("repassword").send_keys("123456789")
    time.sleep(2)
    driver.find_element_by_name("verifyCode").send_keys("2020")
    time.sleep(2)
    driver.find_element_by_class_name("btn save").submit()
    time.sleep(2)
    t = driver.find_element_by_link_text("yanjie123").text
    if item==t:
        print("注册成功")

    driver.quit()


def login():
    driver = StartUp()
    p = public()
    driver.p
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_name("username").send_keys("yanjie000")
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("123123")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/p[3]/span").click()
    time.sleep(5)
    driver.quit()




if __name__ == '__main__':
    login()