"""
功能说明：
配置文件读取
"""
import configparser
import os
class ConfigRead():
    def __init__(self):
        #属性
        #文件的路径
        path_base = os.path.dirname(os.path.dirname(__file__))
        file_path = path_base + "//config" +"//config.ini"
        # print(file_path)
        #实例化对象
        self.conf = configparser.ConfigParser()
        self.conf.read(file_path,encoding="utf-8-sig")
    #读取email -section下的内容
    def reademail(self,option = "all"):
        # 1.读取所有section
        # sects = self.conf.sections()
        # print(sects)
        #2.读取所有的options(名称)
        # options = self.conf.options("email")
        # print(options)
        #3.获取某个section下的所有键值对
        # keyvalues = self.conf.items("email")
        # print(keyvalues)
        # 4.获取某个section下的某个options的值
        # values = self.conf.get("email","smtpserver")
        # print(values)
        if option == "all":
            kvs = self.conf.items("email")
        else:
            kvs = self.conf.get("email",option)
        return kvs
if __name__ == '__main__':
    a = ConfigRead()
    print(a.reademail("sender"))



