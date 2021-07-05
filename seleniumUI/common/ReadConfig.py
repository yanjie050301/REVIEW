"""
 -*- coding: utf-8 -*-
 @File  : ReadConfig.py
 @Author: yanjie
 @Date  : 2021/7/5 0005
 @功能描述  :读取config.ini文件配置参数
 @实现步骤：
    1.导包
    2.命名一个ReadConfig类，
    3.定义方法，方法名为section名字，实现根据传入的option返回对应的option值
"""
import configparser,os
from seleniumUI.common.Public import public
from seleniumUI.common.Log import l
class ReadConfig():
    def __init__(self):
        p = public()
        filedir = p.getdir() + "//config.ini"
        self.c = configparser.ConfigParser()
        self.c.read(filedir,encoding="utf-8")
    def geturl(self,opt = "all"):
        """
        section为url时，获取的相关信息
        :param opt: 根据传入的option的信息，获取option的值
        :return: 返回option的值
        """
        try:
            if opt== "all":
                ovalue = self.c.items("url")
                return ovalue
            else:
                ovalue = self.c.get("url",opt)
                return ovalue
        except Exception as msg:
            l.info(msg)
        finally:
            l.info(f"已成功读取url下的{opt}的值")
    def getemail(self,opt = "all"):
        """
        section为email时，获取的相关信息
        :param opt: 根据传入的option的信息，获取option的值
        :return: 返回option的值
        """
        try:
            if opt== "all":
                ovalue = self.c.items("email")
                return ovalue
            else:
                ovalue = self.c.get("email",opt)
                return ovalue
        except Exception as msg:
            l.info(msg)
        finally:
            l.info(f"已成功读取email下的{opt}的值")
    def getui(self,opt = "all"):
        """
        section为email时，获取的相关信息
        :param opt: 根据传入的option的信息，获取option的值
        :return: 返回option的值
        """
        try:
            if opt== "all":
                ovalue = self.c.items("UI")
                return ovalue
            else:
                ovalue = self.c.get("UI",opt)
                return ovalue
        except Exception as msg:
            l.info(msg)
        finally:
            l.info(f"已成功读取UI下的{opt}的值")
if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.getui())






