from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from UiAutoTest_chao.common.driver import Driver
from UiAutoTest_chao.PO.basePage import BasePage
import time

class MyPage(BasePage):
    #类属性
    my_batton = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[6]/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.TextView")
    my_message = (By.ID,"com.ss.android.article.news:id/f3s")
    def __init__(self,driver):
        self.driver = driver

    def clickmyButton(self):
        self.by_find_element(*self.my_batton).click()
    def get_message_text(self):
        self.clickmyButton()
        t = self.by_find_element(*self.my_message)
        return t.text

if __name__ == '__main__':
    driver = Driver().startUp()
    mp = MyPage(driver)
    print(mp.get_message_text())