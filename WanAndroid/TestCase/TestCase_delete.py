"""
功能介绍：
1.添加删除清单列表接口
"""
import unittest,json
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
from WanAndroid.common.writeexcle import Writeexcle
wr = Readexcle("删除待办清单")
excle_data = wr.getdata()
@ddt
class TestCase_delect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试环境开始")
    def setUp(self):
        print("用例环境开始")
    @data(*excle_data)
    def test_delete(self,values):
        uid = values[3]
        u = values[4]
        url = u+uid+"/json"  #拼接好的url

    def tearDown(self):
        print("用例环境结束")
    def tearDownClass(cls):
        print("测试环境结束")





