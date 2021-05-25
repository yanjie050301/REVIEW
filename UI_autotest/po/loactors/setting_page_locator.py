"""
功能介绍：设置页面
"""



from selenium.webdriver.common.by import By
class SettingPageLocator():
    outlogin_text_loc = (By.ID,"com.lchr.diaoyu:id/rtv_setting_logout")   #退出登录按钮
    outlogin_btn_loc = (By.ID,"android:id/button1")     #确认退出按钮
