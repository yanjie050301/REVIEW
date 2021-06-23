"""
 -*- coding: utf-8 -*-
 @File  : readconfig.py
 @Author: yanjie
 @Date  : 2021/6/15 0015
 @功能描述：读取配置文件
 @实现步骤：
    1.导包
    2.config.ini路径
    3.通过传参获取某个section下的option值
"""
import configparser
import os
from UiAutoTest_chao.common.log import logger
class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        path = os.path.dirname(os.path.dirname(__file__))+"//config.ini"
        self.cf.read(path,encoding="utf-8")
    def readnews(self,option = "all"):
        """
        根据section和option读取内容
        :param option:
        :return:1-items的option的value的键值对组成的元组
        :return: 2-某个section下面option对应的value
        """
        try:
            if option =="all":
                return self.cf.items("news")
            else:
                return self.cf.get("news",option)
        except Exception as msg:
            print(msg)
    def readvivo(self,option = "all"):
        try:
            if option =="all":
                return self.cf.items("vivo")
            else:
                return self.cf.get("vivo",option)
        except Exception as msg:
            print(msg)

    def readxiaomi9(self, option="all"):
        try:
            if option == "all":
                return self.cf.items("xiaomi9")
            else:
                return self.cf.get("xiaomi9", option)
        except Exception as msg:
            print(msg)

    def readserver(self, option="all"):
        try:

            if option == "all":
                return self.cf.items("server")
            else:
                return self.cf.get("server", option)
        except Exception as msg:
            print(msg)

    def reademail(self, option="all"):
        try:

            if option == "all":
                return self.cf.items("email")
            else:
                return self.cf.get("email", option)
        except Exception as msg:
            print(msg)
if __name__ == '__main__':
    r = ReadConfif()
    print(r.reademail())





