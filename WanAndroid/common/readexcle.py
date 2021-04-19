"""
功能介绍：从excle中读取测试数据
步骤：
1.找到excle的路径
2.打开excle
3.依次读取数据,将数据存储到列表中，返回列表
"""
import os,xlrd
"""
#获取上层文件路径
path = os.path.dirname(os.path.dirname(__file__))
#获取文件
new_path = path +"\\data\\" +"excle_login.xls"
f = xlrd.open_workbook(new_path,"encoding=utf-8")
se = f.sheet_by_name("登录接口")
#获取行数
rows = se.nrows
#获取列数
cols = se.ncols
# c = se.row_values(1)
# print(cols)
for a in range(1,rows):
    c = se.row_values(a)
    url = c[2]
    month = c[3]
    data = c[4]

    print(c)
"""
class Readexcle():
    def __init__(self):
        path = os.path.dirname(os.path.dirname(__file__))
        new_path = path +"//data//" +"excle_login.xls"
        f = xlrd.open_workbook(new_path, "encoding=utf-8")
        self.se = f.sheet_by_name("登录接口")
        self.rows = self.se.nrows
        self.datalist = []
    def getdata(self):
        for n in range(1,self.rows):
            data = self.se.row_values(n)
            self.datalist.append(data)
        return self.datalist
if __name__ == '__main__':
    a = Readexcle()
    print(a.getdata())