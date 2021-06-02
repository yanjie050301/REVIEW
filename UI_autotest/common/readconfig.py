"""
功能说明：
读取配置文件
"""
import os,configparser
config_file_path = os.path.dirname(os.path.dirname(__file__)) + "//config.ini"

class Readconfig():
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.cp.read(config_file_path,encoding="utf-8")
    def read_xiaomi9(self,name = "all"):
        try:
            if name == "all":
                values = self.cp.items("xiaomi9")
            else:
                values = self.cp.get("xiaomi9",name)
            return values
        except  Exception as  msg:
            print(msg)
    def read_vivo(self,name = "all"):
        try:
            if name == "all":
                values = self.cp.items("vivo")
            else:
                values = self.cp.get("vivo",name)
            return values
        except  Exception as  msg:
            print(msg)
    def read_app(self,name = "all"):
        try:
            if name == "all":
                values = self.cp.items("app")
            else:
                values = self.cp.get("app",name)
            return values
        except  Exception as  msg:
            print(msg)
    def read_server(self,name = "all"):
        try:
            if name == "all":
                values = self.cp.items("server")
            else:
                values = self.cp.get("server",name)
            return values
        except  Exception as  msg:
            print(msg)
if __name__ == '__main__':
    a = Readconfig()
    print(a.read_app())