"""
功能介绍：
1.添加获取清单列表接口

"""
import unittest,json
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
from WanAndroid.common.writeexcle import Writeexcle
excle = Readexcle("获取清单列表")
excle_data = excle.getdata()
@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试环境准备")
    def setUp(self):
        print("用例环境准备")
    @data(*excle_data)
    def test_get(self,values):
        url = values[3]
        monthd = values[4]
        if excle_data[10] != " ":    #判断是否需要前置条件，cookie
            ht = Httpconfig()
            coo = ht.login()
            ht = Httpconfig(url=url,method=monthd,cookies=coo)
            re = ht.http()


    def tearDown(self):
        print("用例环境结束")
    @classmethod
    def tearDownClass(cls):
        print("测试环境结束")
if __name__ == '__main__':
    unittest.main()




