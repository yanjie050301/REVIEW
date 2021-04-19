"""
功能介绍：
测试用例执行完后，将实际结果写入测试用例的实际结果中
"""
import os,xlrd
from xlutils.copy import copy
class Writeexcle():
    def __init__(self,rows,ncols,data):
        self.rows = rows
        self.ncols = ncols
        self.data = data
        path = os.path.dirname(os.path.dirname(__file__))
        self.new_path = path + "//data//" + "excle_login.xls"
    def writeexcle(self):
        f = xlrd.open_workbook(self.new_path, "encoding = utf-8")
        f1 = copy(f)
        sheet = f1.get_sheet(0)
        sheet.write(self.rows,self.ncols,self.data)

        f1.save(self.new_path)
    def rewrite(self):
        self.writeexcle()
if __name__ == '__main__':
    a = Writeexcle(1,7,9999)
    a.rewrite()





