"""
 -*- coding: utf-8 -*-
 @File  : readExcle.py
 @Author: yanjie
 @Date  : 2021/6/15 0015
 @功能描述  :读取excle，提供对外读取数据的方法，根据提供的类名和方法名获取目标数据
 @实现步骤：
    1.导包xlrd
    2.定义类：
        2-1初始化目标文件
        2-2确定sheet页
        2-3确定测试数据的所有行和列
    3.定义对外方法，通过接收的类名和方法名读取目标测试数据
        3-1匹配则获取同一行的第三列数据
        3-2不匹配则继续：continue
"""
import xlrd
import os
class ReadExcle():
    def __init__(self):
        path = os.path.dirname(os.path.dirname(__file__)) +"//testData//data.xls"
        xl = xlrd.open_workbook(path)
        self.sh = xl.sheet_by_index(0)
        self.rows = self.sh.nrows  #获取表格的行数
        self.colnum = self.sh.ncols  #获取表格的列数

    # 定义对外方法，通过接收的类名和方法名读取目标测试数据
    def read(self,classname,monthname):
        #遍历表格判断所有列中的类名和方法名
        for i in range(1,self.rows):
            #获取第一列的类名
            c_name = self.sh.cell_value(i,0)
            # 获取第二列的方法名
            m_name = self.sh.cell_value(i,1)
            #判断
            if c_name == classname and m_name == monthname:
                data = self.sh.cell_value(i,2)
                return data
            else:
                continue
if __name__ == '__main__':
    r =ReadExcle()
    print(r.read("LittleMessageTest","test_samll_message_normal"))





