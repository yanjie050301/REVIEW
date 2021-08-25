"""
 -*- coding: utf-8 -*-
 @File  : lainxi.py
 @Author: yanjie
 @Date  : 2021/8/13 0013
 @功能描述  :练习log
 @实现步骤：
    1.
    2.
    3.
"""
import logging
def Log():
    logging.basicConfig(level=logging.INFO,format="%(name)s--第%(lineno)s行--日志级别为%(levelname)s--log信息：%(message)s")
    logger = logging.getLogger("日志名称")
    return logger
if __name__ == '__main__':
    l = Log()
    l.debug("jjjj")

