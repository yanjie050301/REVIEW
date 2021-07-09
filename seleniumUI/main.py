
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from seleniumUI.common.Public import public
def StartUp():
    option = webdriver.ChromeOptions()
    option.add_argument(r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
    global driver
    driver = webdriver.Chrome(chrome_options=option)
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
    item = "yanjie143"
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/input[1]").send_keys(item)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/input[2]").send_keys("123456789")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/input[3]").send_keys("123456789")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/input[4]").send_keys("2020")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/p[3]/span").click()
    time.sleep(2)
    t = driver.find_element_by_link_text(item).text
    if item==t:
        print("注册成功")
    driver.quit()


def login():
    driver = StartUp()
    p = public()
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    name = "yanjie000"
    driver.find_element_by_name("username").send_keys(name)
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("123123")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/p[3]/span").click()
    print("登录成功！！！")
    # page = driver.page_source
    # num = page.find("yanjie000")
    # if num != -1:
    #     print("登录成功")
    time.sleep(3)
    # time.sleep(2)
    # driver.find_element_by_link_text("退出登录").click()
    # time.sleep(5)
    # driver.quit()
def get_element():
    driver = StartUp()
    text = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[2]/a[1]").text
    page = driver.page_source
    print("测试测试:",text)
def ation():
    driver = StartUp()
    username = driver.find_element_by_link_text("yanjie000")
    ActionChains(driver).move_to_element(username).perform()
def close():
    driver = StartUp()
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/h2/b").click()
    driver.quit()
def savensermsg():
    login()
    driver.find_element_by_link_text("待办清单").click()
    time.sleep(2)
    t = driver.find_element_by_link_text("已完成清单").text
    if t == "已完成清单":
        print("进入待办清单页面成功")
if __name__ == '__main__':

    # get_element()
    # login()
    # register()
    close()
