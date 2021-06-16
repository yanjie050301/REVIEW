
from UiAutoTest_chao.common.driver import Driver

class Public():
    def __init__(self,driver):
        self.driver = driver
    #获取屏幕尺寸
    def getsize(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return (x,y)
    #上滑
    def swipeup(self,t=1000):
        size = self.getsize()
        x1 = int(size[0]*0.5)
        y1 = int(size[1]*0.25)
        y2 = int(size[1] * 0.75)
        self.driver.swipe(x1,y1,x1,y2,duration=t)
    #下滑
    def swipedown(self,t=1000):
        size = self.getsize()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.75)
        y2 = int(size[1] * 0.25)
        self.driver.swipe(x1,y1,x1,y2,duration=t)
    #左滑
    def swipeleft(self,t=1000):
        size = self.getsize()
        x1 = int(size[0]*0.75)
        x2 = int(size[0]*0.25)
        y = int(size[1] * 0.5)
        self.driver.swipe(x1,y,x2,y,duration=t)
    #右滑
    def swiperight(self,t=1000):
        size = self.getsize()
        x1 = int(size[0] * 0.25)
        x2 = int(size[0] * 0.75)
        y = int(size[1] * 0.5)
        self.driver.swipe(x1, y, x2, y, duration=t)
if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()
    p = Public(driver)
    print(p.getsize())
