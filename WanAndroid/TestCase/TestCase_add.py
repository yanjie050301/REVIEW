"""
功能介绍：
1.添加待办清单接口
2.使用unittest框架，执行测试用例
"""
import unittest,json,time
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
        t = time.strftime("%Y-%m-%d")  #获取当前的年月日
        print(f"当前时间为{t}")
        url = values[3]
        method = values[4]
        prams = eval(values[5])
        prams["date"] = t   #提交的时间更改为当前的年月日
        ht = Httpconfig()
        coo = ht.login()    #获取用户登录的cookie
        htt = Httpconfig(url,method,prams,coo)
        re = htt.http()     #请求接口
        print(re)
        eyuqi = values[6]  # 获取预期结果
        cyuqi = values[6].encode("utf-8")  # 获取预期结果.中文需要编码
        status_code = re[1]    #获取服务器返回的状态码
        # eval无法解析null， true， false之类的数据
        global false, null, true
        false = null = true = ''
        re_json = eval(re[0])  # 获取服务器返回的数据，类型为dict
        errorMsg = re_json.get("errorMsg")#获取服务器返回的错误信息
        errorMsg1 = re_json.get("errorMsg").encode("utf-8")   #获取服务器返回的错误信息.中文需要编码
        id = int(values[0])  #获取测试用例的id
        wr = Writeexcle(1)
        wr_get = Writeexcle(2)    #将服务器返回数据的title值写去获取列表中的预期结果位置
        wr_complete = Writeexcle(3)  #将服务器返回数据的清单id值写去完成清单列表中的uid位置
        wr_delete = Writeexcle(4)    #将服务器返回数据的清单id值写去删除清单列表中的uid位置
        if errorMsg !="":
            wr.rewrite(id, 7, eyuqi)
            wr.rewrite(id, 8, status_code)
            if cyuqi == errorMsg1:
                wr.rewrite(id,9,"pass")
            else:
                wr.rewrite(id,9,"fail")
            self.assertEqual(cyuqi,errorMsg1,msg="用例失败")
        else:
            title = re_json.get("data").get("title")  # 获取实际结果
            qingdan_id = re_json.get("data").get("id")
            print("555555555555",type(title))

            wr.rewrite(id,7, title)
            wr.rewrite(id,8, status_code)
            if title == eyuqi:
                wr.rewrite(id,9,"pass")
            else:
                wr.rewrite(id,9,"fail")
            self.assertEqual(eyuqi, title, msg="用例失败")
            if id in range(1,5):
                wr_get.rewrite(id, 6, title)  # 将服务器返回数据的title值写去获取列表中的预期结果位置,只写前4条数据的值
                wr_complete.rewrite(id,3,qingdan_id)      #将服务器返回数据的清单id值写去完成清单列表中的uid位置
                wr_delete.rewrite(id, 3, qingdan_id)     #将服务器返回数据的清单id值写去删除清单列表中的uid位置

    def tearDown(self):
        print("用例环境结束")
    def tearDownClass(cls):
        print("测试环境结束")
unittest.main
# if __name__ == '__main__':
#     unittest.main()





