"""
功能介绍
"""

from base_page import BasePage
from loactors.login_page_loctor import LoginPageLocator
from loactors.mine_page_locator import MinePageLocator
from loactors.setting_page_locator import SettingPageLocator
class LoginPage(BasePage):
    def login(self,username,password):
        self.send_data(LoginPageLocator.username_input_loc,username,msg="用户名输入框")
        self.send_data(LoginPageLocator.password_input_loc,password,msg="密码输入框")
        self.click_element(LoginPageLocator.login_btn_loc,msg="登录按钮")
    def is_user_login(self,msg):
        if self.search_element(MinePageLocator.nickname_loc,msg):   #判断是否存在名称，存在表示登录状态，返回TRUE
            return True
        else:
            return False
    def loginout(self):
        self.click_element(MinePageLocator.setting_icon_loc,msg="设置按钮")
        self.click_element(SettingPageLocator.outlogin_text_loc,msg="退出登录按钮")
        self.click_element(SettingPageLocator.outlogin_btn_loc,msg="确定退出按钮")
    def go_to_login_page(self):
        if self.is_user_login():
            self.loginout()
        self.click_element(MinePageLocator.click_login_text_loc,msg="点击登录按钮")
        self.click_element(LoginPageLocator.account_login_text_loc,msg="钓鱼人账号登录按钮")
    def get_element_text(self,loc,msg=""):
        return self.search_element(MinePageLocator.nickname_loc,msg).text

if __name__ == '__main__':
    pass


