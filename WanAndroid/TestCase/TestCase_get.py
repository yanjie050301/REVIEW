"""
功能介绍：
1.添加获取清单列表接口

"""
import unittest,json,re
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
        if values[10] != "":    #判断是否需要前置条件，cookie
            ht = Httpconfig()
            coo = ht.login()
            ht = Httpconfig(url=url,method=monthd,cookies=coo)
            result = ht.http()
            expected_results = values[6]    #获取预期结果
            status = result[1]  # 获取接口的状态码
            try:
                result = str(result)
                ex = re.compile(r""+expected_results+"")
                actual_r = ex.search(result)
                actual_results = actual_r.group()    #实际结果
            except Exception as msg:
                print("正则匹配结果为",msg)
                actual_results = "正则失败"
            id = values[0]
            wr = Writeexcle(2)
            wr.rewrite(id, 7, actual_results)
            wr.rewrite(id, 8, status)
            if actual_results ==expected_results:
                wr.rewrite(id,9,"pass")
            else:
                wr.rewrite(id, 9, "fail")
            self.assertEqual(actual_results,expected_results,msg="用例失败")
    def tearDown(self):
        print("用例环境结束")
    @classmethod
    def tearDownClass(cls):
        print("测试环境结束")
# unittest.main
if __name__ == '__main__':
    unittest.main()




