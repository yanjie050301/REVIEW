"""
ddt框架的练习
1.ddt框架的作用：用于依次读取测试数据去请求接口，一般用于页面有输入框，输入不同组数据验证不同的测试结果
2.ddt用法：@data（测试数据），仅适用于传入一个参数
            @unpack  分发器，适用于传入多个参数
"""
from ddt import ddt,data,unpack
import unittest
li = [5,6,7]
testdate = [[8,9],[10,11]]
@ddt          #ddt框架要结合unittest框架进行使用，必须放在类的前面
class Test(unittest.TestCase):
    # @data(1)    #一次传入一个参数
    # def testa(self,r):
    #     print(r)
    #     # self.assertEqual(value,value-1)
    # @data(2,3,4)    #一次传入多个参数
    # def testb(self,r):
    #     print(r)
    # @data(*li)     #传入可变参数
    # def testc(self,r):
    #     print(r)
    @data((1,1))     #单次执行，单次传递多个参数，多个参数作为一个整体传入
    def testd(self,r):
        print(r)
    @data((1,1),(2,2))    #多次执行，传递两次参数，第一次是（1,1），第二次是（2,2）
    def teste(self,r):
        print(r)
# unittest.main
if __name__ == '__main__':
    unittest.main()









