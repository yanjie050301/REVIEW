"""
功能介绍：从excle中读取测试数据
步骤：
1.找到excle的路径
2.打开excle
3.依次读取数据
"""
import os,xlrd
path = os.path.dirname(os.path.dirname(__file__))
new_path = path +"//data"
files = os.listdir(new_path)
print(files)

# class Readexcle():
#     def __init__(self):
#         self.path = os.path.dirname(__file__)