"""
@Time : 2021/6/5 16:40
@Author : 远秋
@Email : gongyuanqiu@163.com
@File : public.py
@Project : AppUIAutomation
@feature : 
@实现步骤：
"""
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#上划
def swipeUp(driver,t=1000):
    size = getSize(driver)
    x1 = int(size[0] * 0.5) #x 坐标
    y1 = int(size[1] * 0.75) #起始 y 坐标
    y2 = int(size[1] * 0.25) #终点 y 坐标
    driver.swipe(x1, y1, x1, y2,duration=t)

#下滑
def swipeDown(driver,t=1000):
    size = getSize(driver)
    x1 = int(size[0] * 0.5) #x 坐标
    y1 = int(size[1] * 0.25) #起始 y 坐标
    y2 = int(size[1] * 0.75) #终点 y 坐标
    driver.swipe(x1, y1, x1, y2,duration=t)

#屏幕向左滑动
def swipLeft(driver,t=1000):
    size = getSize(driver)
    x1=int(size[0]*0.75)
    y1=int(size[1]*0.5)
    x2=int(size[0]*0.05)
    driver.swipe(x1,y1,x2,y1,duration=t)

#屏幕向右滑动
def swipRight(driver,t=1000):
    size = getSize(driver)
    x1=int(size[0]*0.05)
    y1=int(size[1]*0.5)
    x2=int(size[0]*0.75)
    driver.swipe(x1,y1,x2,y1,duration=t)