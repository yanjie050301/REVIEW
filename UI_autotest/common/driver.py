"""
功能说明：
创建一个session（会话）
步骤：
1.读取config.ini文件获取传入APP启动参数，传给remote方法
2.返回driver供其他方法使用

"""
from appium import webdriver
from UI_autotest.common.readconfig import Readconfig
import time
class Driver():
    def __init__(self):
        co = Readconfig()
        self.platformName = co.read_app("platformName")
        self.platformVersion = co.read_vivo("platformVersion")
        self.deviceName = co.read_vivo("deviceName")
        # self.platformVersion = co.read_xiaomi9("platformVersion")
        # self.deviceName = co.read_xiaomi9("deviceName")
        self.appPackage = co.read_app("appPackage")
        self.appActivity = co.read_app("appActivity")
        self.app = co.read_app("app")
        self.port = co.read_server("port")
        self.ip = co.read_server("ip")
    def start_session(self):
        desired_caps = {
            "platformName": self.platformName,
            "platformVersion": self.platformVersion,
            "deviceName": self.deviceName,
            "appPackage": self.appPackage,
            "appActivity": self.appActivity,
            "app": self.app,
            "skipServerInstallation": False,  #禁止重复安装两个应用(oi.appium.uiautomator2.server和oi.appium.uiautomator2.server.test)
            "noReset": True    #禁止重复安装测试APP应用
        }

        url = "http://" + self.ip +":"+ self.port+"/wd/hub"

        driver = webdriver.Remote(url, desired_caps)
        return driver
if __name__ == '__main__':
    a = Driver()
    driver = a.start_session()
    time.sleep(5)
    driver.quit()
