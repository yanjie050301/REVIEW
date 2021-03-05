"""
功能介绍：
1.打开excel文件
2.按照坐标将测试数据写入excel对应的实际结果中
"""
import os
import xlrd
from xlutils.copy import copy
#获取当前路径
path = os.getcwd()
#获取当前路径的上一级路径
base_path = os.path.dirname(path)
#拼接路径为写入的excel文件路径
file_path = base_path + "\\TestData" + "\\data.xls"
class WriteExcel():
    def __init__(self,id,real,status):    #id表示写入的行号，real表示实际结果，status表示请求接口的状态
        self.status = status
        self.real = real
        self.id = id
    def write_excle(self):
        # 打开文件
        f = xlrd.open_workbook(file_path)
        # 复制文件
        write_e = copy(f)
        # 获取文件的sheet
        write_sheet = write_e.get_sheet(0)
        # 写入数据,接口的实际结果
        write_sheet.write(self.id,6,self.real)
        #写入接口的请求状态
        write_sheet.write(self.id,7,self.status)
        # 保存文件
        write_e.save(file_path)
    def save_e(self):
        #每次调用最新的excle表格，保证之前写入的不被覆盖掉
        self.write_excle()
if __name__ == '__main__':

    for i in range(1,5):
        a = WriteExcel(i,"ss","ddd")
        a.save_e()