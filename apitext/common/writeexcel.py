"""
功能介绍：
1.打开excel文件
2.按照坐标将测试数据写入excel对应的实际结果中
"""
import xlwt,os
#获取当前路径
path = os.getcwd()
#获取当前路径的上一级路径
base_path = os.path.dirname(path)
#拼接路径为写入的excel文件路径
file_path = base_path + "\\TestData" + "\\data.xls"
class WriteExcel():
    def __init__(self,real):
        #打开文件
        self.f = open(file_path,"+r",encoding="utf-8")
        self.real = real
    def write_excle(self):
        pass