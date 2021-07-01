from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from UiAutoTest_chao.common.driver import Driver
import time
from UiAutoTest_chao.PO.basePage import BasePage
from UiAutoTest_chao.common.readExcle import ReadExcle
class HomePage(BasePage):
    #定义页面类属性，就是元素属性
    publish_button = (By.ID,"com.ss.android.article.news:id/d20")   #发布按钮
    little_message = (By.ID,"com.ss.android.article.news:id/cte")   #微头条按钮
    send_text = (By.ID,"com.ss.android.article.news:id/ao7")      #输入框
    submit_button = (By.ID,"com.ss.android.article.news:id/dxy")    #提交信息发布按钮
    # 首页按钮
    fristpage = (By.ID,"com.ss.android.article.news:id/c0p")
    def __init__(self,driver):
        self.driver = driver
    def clickFristBatton(self):
        self.by_find_element(*self.fristpage).click()
    def clickPublishButton(self):
        self.by_find_element(*self.publish_button).click()  #使用显示等待，直到元素被定位到才进行操作
    def clickLittleMessage(self):
        self.by_find_element(*self.little_message).click()
    def sendtext(self,text):
        self.by_find_element(*self.send_text).send_keys(text)
    def clicksubmitbutton(self):
        self.by_find_element(*self.submit_button).click()
    def publish_article(self,text):
        self.clickPublishButton()
        self.clickLittleMessage()
        self.sendtext(text)
        self.clicksubmitbutton()
if __name__ == '__main__':
    driver = Driver().startUp()
    data = int(ReadExcle().read("LittleMessageTest","test_samll_message_normal"))
    hp = HomePage(driver)
    print(hp.gettext())
    driver.quit()