"""
功能介绍：
测试用例执行完后，将实际结果写入测试用例的实际结果中
"""
import os,xlrd
from xlutils.copy import copy


path = os.path.dirname(os.path.dirname(__file__))
new_path = path + "//data//" + "excle_login.xls"
f = xlrd.open_workbook(new_path,"encoding = utf-8")
f1 = copy(f)
sheet = f1.get_sheet(0)
sheet.write(1,6,8888)
f1.save(new_path)
class Writeexcle():
    def __init__(self,actual_results,):






