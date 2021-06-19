from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from UiAutoTest_chao.common.driver import Driver
import time

class HomePage():
    #类属性
    publish_button = (By.ID, "com.ss.android.article.news:id/bpx")
    little_message = (By.ID, "com.ss.android.article.news:id/bpx")

    def __init__(self,driver):
        self.driver = driver

    def clickPublishButton(self):
        self.driver.find_element(*self.publish_button).click()
        time.sleep(5)

    def clickLittleMessage(self):
        self.driver.find_element(*self.little_message).click()
        time.sleep(5)

if __name__ == '__main__':
    driver = Driver().startUp()
    hp = HomePage(driver)
    hp.clickPublishButton()
    hp.clickLittleMessage()