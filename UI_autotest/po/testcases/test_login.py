"""
登录成功失败，测试类
"""
from UI_autotest.common.base import Base
from UI_autotest.po.pages.login_page import LoginPage
class TeatLogin(Base):
    def test_login_success(self,username,password):
        self.lp.go_to_login_page()
        self.lp.login(username,password)
        self.assertEquals("闫洁666",self.lp.get_element_text("用户名称"))

if __name__ == '__main__':
    a = TeatLogin
    a.test_login_success()

