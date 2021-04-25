"""
ddt框架的练习
1.ddt框架的作用：用于依次读取测试数据去请求接口，一般用于页面有输入框，输入不同组数据验证不同的测试结果
2.ddt用法：@data（测试数据），仅适用于传入一个参数
            @unpack  分发器，适用于传入多个参数
"""
from ddt import ddt,data,unpack
import unittest
@ddt          #ddt框架要结合unittest框架进行使用，必须放在类的前面
class Test(unittest.TestCase):


    @data((2,3),(3,4))
    # @unpack
    def testa(self,r):
        print(r)
        # self.assertEqual(value,value-1)
if __name__ == '__main__':
    unittest.main()









