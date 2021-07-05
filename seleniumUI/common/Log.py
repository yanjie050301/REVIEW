"""
 -*- coding: utf-8 -*-
 @File  : Log.py
 @Author: yanjie
 @Date  : 2021/7/5 0005
 @功能描述  :应用到每一个py文件中，代替print打印调试
 @实现步骤：
    1.导包logging
    2.定义一个方法，使用logging的baseconfig方法进行log信息配置
    3.定义日志名称，使用logging.getlogger在输出日志时候显示
 @log等级划分：（规则：已设置的log级别为准，该级别以上的log信息都可以打印）
    1.CRITICAL 严重
    2.ERROR  错误
    3.WARNING  警告
    4.INFO 信息
    5.DEBUG  调试
 @说明：
 basicConfig中format参数说明，在basicConfig文件中第485行左右
 @log相对于print的优点：
    1.log打印信息的方式既可以控制台输出，也可以已文件的形式输出，print只能控制台输出
    2.log打印可以进行等级划分，控制log信息打印的等级

"""
import logging
def log():
    logging.basicConfig(level=logging.INFO,format="%(asctime)s-第%(lineno)d行-%(levelname)s信息打印：%(message)s")
    log = logging.getLogger("ceshi:")
    return log
l = log()   #提前实例化，再次调用的时候就不需要实例化，
if __name__ == '__main__':
    l.info("3333")





