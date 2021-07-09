"""
 -*- coding: utf-8 -*-
 @File  : ReadExcle.py
 @Author: yanjie
 @Date  : 2021/7/9 0009
 @功能描述  :封装读取表格中的测试数据
 @实现步骤：
    1.导包
    2.打开文件
    2.获取sheet
    3.获取sheet中单元格内容
"""
import xlrd
from seleniumUI.common.Public import public
class ReadExcle():
    p = public()
    path = p.getdir() + "\\TestData\\data.xls"
    xl = xlrd.open_workbook(path)
    sh = xl.sheet_by_index(0)
    def getvalue(self,className,methodName):
        """
        获取对应的信息
        :param className: 类名
        :param methodName: 方法名
        :return:以用户名和密码组成的元组
        """
        rows =self.sh.nrows
        for r in range(1,rows+1):
            v = self.sh.row_values(r)
            c_name = v[0]   #获取第一行类名
            m_name = v[1]  #获取第二行方法名
            if c_name == className and m_name  == methodName:
                return v[2],v[3]
                break
if __name__ == '__main__':
    re = ReadExcle()
    className = "LoginTest"
    methodName = "test_login_normal"
    m = re.getvalue(className,methodName)
    print(int(m[1]))





