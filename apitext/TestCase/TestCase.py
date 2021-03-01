"""
功能描述：
1.调用readExcel模块，读取册数数据
2.根据测试数据中每个接口的请求方式，进行对应的请求

"""


import unittest
import requests
from common.readexcel import ReadExcel
read_excel = ReadExcel()
read_data = read_excel.resd_exc
print(read_excel.resd_exc)
# class TestCase(unittest.TestCase):
#     #1.初始化方法
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("cehsikaishi")
#         #1.调用ReadExcel模块，读取测试数据
#
#     def test_a(self):
#         print("dddd")
#     @classmethod
#     def tearDownClass(cls):
#         print("ceshijieshu")
# if __name__ == '__main__':
#     unittest.main()




