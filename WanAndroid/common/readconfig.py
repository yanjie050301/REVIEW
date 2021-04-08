import configparser
import os
"""
1、查找config.ini的路径
2、传值option和section获取相关信息的信息

"""
#获取config文件夹上级的地址
# path = os.path.dirname(os.path.dirname(__file__))
#拼接config.ini文件地址
# new_path = path +"\\config\\config.ini"
#实例化configparser
# conf=configparser.ConfigParser()
#读取config.ini文件
# conf.read(new_path,encoding="utf-8")
#获取所以的sections
# sections = conf.sections()
#获取某个section下的所有options
# options = conf.options("host")
#获取某个section下的多有options的键值对
# value = conf.items("host")
#获取某个section的options的值
# gets = conf.get("host","uu")
# print(gets)

class Readconfig():
    def __init__(self,sec):
        self.sec = sec
        path =os.path.dirname(os.path.dirname(__file__)) #获取config文件夹上级的地址
        self.new_path = path + "\\config\\config.ini"   #拼接config.ini文件地址
        self.conf = configparser.ConfigParser()
    def readcon(self,opt):
        self.conf.read(self.new_path,encoding="utf-8")
        data = self.conf.get(self.sec,opt)    #获取具体的section下的某个option的值
        return data


if __name__ == '__main__':
    a = Readconfig("host")
    a.readcon("uu")