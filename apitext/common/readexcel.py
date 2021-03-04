"""
功能描述：
    1、打开exce
    2、获取sheet页
    3、定位行和列，读数据
    4、循环读取每一行数据
    5、组装测试数据，返回key：value的形式

"""
import xlrd
import os
# current_dir = os.path.abspath(__file__)     #__file__表示当前文件，  abspath带文件后缀名的路径
# print(current_dir)
path = os.getcwd()    #获取当前路径
base_dir = os.path.dirname(path)   #获取当前路径的上一层路径
# print(base_dir)


class ReadExcel():
    #属性
    def __init__(self):
        self.excel_dir = base_dir + "\\TestData" + "\\data.xls"    #组装excel路径
        #打开excel
        self.exc = xlrd.open_workbook(self.excel_dir)
        #定位sheet页
        self.sheet = self.exc.sheet_by_name("testdata")
    def read_exc(self):
        #读取测试数据
        #获取列表的行和列
        nrows = self.sheet.nrows
        ncols = self.sheet.ncols
        #定义一个新列表，存放以字典形式的测试数据
        datalist = []
        #按行读取
        for n in range(1,nrows):
            #读取第一行数据喂字典的key值
            key_value = self.sheet.row_values(0)
            value_value = self.sheet.row_values(n)
            #循环使用字典推导式进行组装，将表头与数据进行一一对应
            dict_exc = {key_value[j]:value_value[j] for j in range(ncols)}
            datalist.append(dict_exc)
        # print(datalist)
        return datalist
if __name__ == '__main__':
    rec = ReadExcel()
    rec.read_exc()
"""
[{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'zhuxiaodong','password':'test01'}", 'expect': '0', 'real': '', 'status': ''},
 {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'zxd01','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''}, 
 {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'Get', 'value': "{'username':'zhuxiaodong'}", 'expect': '0', 'real': '', 'status': ''}]
"""


