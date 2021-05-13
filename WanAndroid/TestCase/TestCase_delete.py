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
        uid = str(int((values[3])))      #从表格中获取id值为float，需要转化为int类型在转化为string类型，方便后面url的拼接
        u = values[4]
        url = u+uid+"/json"  #拼接好的url
        method = values[5]
        ht = Httpconfig()
        coo = ht.login()     #获取用户登录的cookie
        re = Httpconfig(url,method,cookies=coo)
        r = re.http()
        status = r[1]   #获取接口请求状态
        # eval无法解析null， true， false之类的数据
        global false, null, true
        false = null = true = ''
        r_json = eval(r[0])     #获取服务器返回的数据，类型为dict
        actual_results = r_json.get("errorCode")     #获取服务器返回的错误码
        id = values[0]   #获取表格id
        expected_results = int(values[7])   #获取预期结果
        w = Writeexcle(3)
        w.rewrite(id,8,actual_results)
        w.rewrite(id,9,status)
        if expected_results == actual_results:
            w.rewrite(id,10,"pass")
        else:
            w.rewrite(id,10,"fail")
        self.assertEqual(expected_results,actual_results,msg="用例失败")
    def tearDown(self):
        print("用例环境结束")
    def tearDownClass(cls):
        print("测试环境结束")
# unittest.main
if __name__ == '__main__':
    unittest.main()



