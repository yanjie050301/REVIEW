"""
功能介绍：
1.登录接口
2.使用unittest框架，执行测试用例
"""
import unittest,json
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
from WanAndroid.common.writeexcle import Writeexcle
from WanAndroid.common.logconfig import Logconfig
excle_login = Readexcle("登录接口")
excle_data_login = excle_login.getdata()   #一个大列表嵌套测试数据的小列表
@ddt
class Wanandroid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")
    def setUp(self):
        print("每条测试用例开始")
    @data(*excle_data_login)
    def test_login(self,value):
        url = value[3]
        method = value[4]
        params = eval(value[5])
        ht = Httpconfig(url,method,params)
        re = ht.http()
        #eval无法解析null， true， false之类的数据
        global false, null, true
        false = null = true = ''
        re_json = eval(re[0]) #获取服务器返回的数据，类型为dict
        errorCode = re_json.get("errorCode")  #获取返回值的errorCode的值，实际结果
        status_code = re[1]        #获取响应状态码
        expected_results = int(value[6])#获取测试用例中预期结果的值

        id = int(value[0])        #获取测试用例的id
        try:
            wr = Writeexcle(0)
            if expected_results == errorCode:
                wr.rewrite(id,7,errorCode)
                wr.rewrite(id,8,status_code)
                wr.rewrite(id,9,"pass")
            elif expected_results != errorCode:
                wr.rewrite(id, 7, errorCode)
                wr.rewrite(id, 8, status_code)
                wr.rewrite(id, 9, "fail")
        except Exception as msg:
            print(f"报错信息为{msg}")
        else:
            print("写入表格成功")
        finally:
            log = Logconfig()
            log.info("登录用例执行完毕")
        # 断言预期结果与实际结果是否一致
        self.assertEqual(expected_results, errorCode, msg="用例失败")
    def tearDown(self):
        print("每条测试用例结束")
    @classmethod
    def tearDownClass(cls):
        print("测试结束")
# unittest.main
if __name__ == '__main__':
    unittest.main()
