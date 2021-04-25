"""
功能介绍：
1.添加待办清单接口
2.使用unittest框架，执行测试用例
"""
import unittest,json
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
from WanAndroid.common.writeexcle import Writeexcle
data_add = Readexcle("添加待办清单")
datas_add = data_add.getdata()   #从excle获取待办清单的数据
@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试环境准备")
    def setUp(self):
        print("用例环境准备")
    @data(*datas_add)
    def test_add(self,values):
        """
        这个功能也没用啊！！！
        :param string:
        :return:
        """
        url = values[3]
        method = values[4]
        prams = eval(values[5])
        ht = Httpconfig()
        coo = ht.login()    #获取用户登录的cookie
        htt = Httpconfig(url,method,prams,coo)
        re = htt.http()     #请求接口
        print(re)
        eyuqi = values[6]  # 获取预期结果
        cyuqi = values[6].encode("utf-8")  # 获取预期结果.中文需要编码
        status_code = re[1]    #获取服务器返回的状态码
        errorMsg = re[0]["errorMsg"]#获取服务器返回的错误信息
        errorMsg1 = re[0]["errorMsg"].encode("utf-8")   #获取服务器返回的错误信息.中文需要编码
        id = int(values[0])  #获取测试用例的id
        wr = Writeexcle(1)
        if errorMsg !="":
            wr.rewrite(id, 7, eyuqi)
            wr.rewrite(id, 8, status_code)
            if cyuqi == errorMsg1:
                wr.rewrite(id,9,"pass")
            else:
                wr.rewrite(id,9,"fail")
            self.assertEqual(cyuqi,errorMsg1,msg="用例失败")
        else:
            title = re[0]["data"]["title"]  # 获取实际结果
            wr.rewrite(id,7, title)
            wr.rewrite(id,8, status_code)
            if title == eyuqi:
                wr.rewrite(id,9,"pass")
            else:
                wr.rewrite(id,9,"fail")
            self.assertEqual(eyuqi, title, msg="用例失败")

    def tearDown(self):
        print("用例环境结束")
    def tearDownClass(cls):
        print("测试环境结束")
# unittest.main
if __name__ == '__main__':
    unittest.main()





