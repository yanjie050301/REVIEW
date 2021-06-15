"""
 -*- coding: utf-8 -*-
 @File  : log.py
 @Author: yanjie
 @Date  : 2021/6/15 0015
 @功能描述  :log文件配置
 @实现步骤：
    1.
    2.
    3.
"""
import logging
def Log():
    logging.basicConfig(level=logging.DEBUG,format="%(name)s-%(levelname)s-%(filename)s.py-第%(lineno)d行:%(message)s")
    logger = logging.getLogger("appium-UI")
    return logger
logger = Log()    #提前实例化
if __name__ == '__main__':
    # logger = Log()
    logger.info("kkkkk")



