"""
功能介绍：登录页面
步骤：
1.导入By包
2.把具体的预算定位写到类里
"""


from selenium.webdriver.common.by import By
class LoginPageLocator():
    
    account_login_text_loc = (By.ID,"com.lchr.diaoyu:id/tv_account_login")   #切换钓鱼人账号登录
    username_input_loc= (By.ID,"com.lchr.diaoyu:id/user_id")     #用户名输入
    password_input_loc = (By.ID,"com.lchr.diaoyu:id/passwd_id")    #密码输入
    login_btn_loc = (By.ID,"	com.lchr.diaoyu:id/btn_login")    #登录按钮