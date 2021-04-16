"""
功能介绍：
使用unittest框架，执行测试用例
"""
import unittest
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
excle = Readexcle()
excle_data = excle.getdata()   #一个大列表嵌套测试数据的小列表
@ddt()
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")
    def setUp(self):
        print("每条测试用例开始")
    @data(*excle_data)
    def test_case(self,value):
        url = value[2]
        month = value[3]
        data1 = eval(value[4])
        ht = Httpconfig(url,month,data1)
        re = ht.http()
        errorCode = re["errorCode"]   #获取返回值的errorCode的值
        expected_results = int(value[5])#获取测试用例中预期结果的值
        #断言预期结果与实际结果是否一致
        self.assertEqual(expected_results,errorCode,msg="用例失败")
    def tearDown(self):
        print("每条测试用例结束")
    @classmethod
    def tearDownClass(cls):
        print("测试结束")
if __name__ == '__main__':
    unittest.main()
