


def getsize(driver):
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return (x,y)
def swipeup(driver,t=1000):
    size = getsize(driver)
    x1 = int(size[0]*0.5)
    y1 = int(size[1]*0.75)
    y2 = int(size[1] * 0.25)
    driver.swipe(x1,y1,x1,y2,duration=1000)
