from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
def email():
    driver.get(url="https://www.126.com/")
    time.sleep(3)
    driver.switch_to.frame(0)    #进入iframe框架
    driver.find_element_by_xpath("//form/div/div[1]/div[2]/input").send_keys("123455@126.com")
    time.sleep(3)
    driver.switch_to.default_content()#退出框架
def xiecheng():
    driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")
    time.sleep(3)
    h = driver.find_element_by_id("J_roomCountList")
    # h.find_element_by_xpath("/html/body/div[9]/div/div[1]/form[1]/div[3]/div[1]/select/option[2]").click()
    # Select(h).select_by_index(5)
    # Select(h).select_by_value("3")
    Select(h).select_by_visible_text("10间")
    time.sleep(5)


    driver.quit()
if __name__ == '__main__':
    xiecheng()