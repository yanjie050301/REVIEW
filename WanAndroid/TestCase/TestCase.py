"""
功能介绍：
使用unittest框架，执行测试用例
"""
import unittest
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
from WanAndroid.common.writeexcle import Writeexcle
excle = Readexcle("登录接口")
excle_data = excle.getdata()   #一个大列表嵌套测试数据的小列表

@ddt
class Wanandroid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")
    def setUp(self):
        print("每条测试用例开始")
    @data(*excle_data)
    def test_login(self,value):
        """ 说好的惊喜呢"""
        url = value[3]
        month = value[4]
        params = eval(value[5])
        ht = Httpconfig(url,month,params)
        re = ht.http()
        errorCode = re[0]["errorCode"]   #获取返回值的errorCode的值，实际结果
        status_code = re[1]        #获取响应状态码
        expected_results = int(value[6])#获取测试用例中预期结果的值

        id = int(value[0])        #获取测试用例的id
        try:
            if expected_results == errorCode:
                wr = Writeexcle(id,7,errorCode)
                wr.rewrite()
                wr = Writeexcle(id, 8, status_code)
                wr.rewrite()
                wr = Writeexcle(id, 9, "pass")
                wr.rewrite()
            elif expected_results != errorCode:
                wr = Writeexcle(id, 7, errorCode)
                wr.rewrite()
                wr = Writeexcle(id, 8, status_code)
                wr.rewrite()
                wr = Writeexcle(id, 9,"fail")
                wr.rewrite()
        except Exception as msg:
            print(f"报错信息为{msg}")
        else:
            print("写入表格成功")
        finally:
            print("执行完毕")
        # 断言预期结果与实际结果是否一致
        self.assertEqual(expected_results, errorCode, msg="用例失败")
    def test_add(self):
        pass
    def tearDown(self):
        print("每条测试用例结束")
    @classmethod
    def tearDownClass(cls):
        print("测试结束")
if __name__ == '__main__':
    unittest.main()
