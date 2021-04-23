"""
功能介绍：
使用unittest框架，执行测试用例
"""
import unittest
from ddt import ddt,data
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.httpconfig import Httpconfig
from WanAndroid.common.writeexcle import Writeexcle
excle_login = Readexcle("登录接口")
excle_data_login = excle_login.getdata()   #一个大列表嵌套测试数据的小列表
excle_add = Readexcle("添加待办清单")
excle_data_add = excle_add.getdata()
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
        month = value[4]
        params = eval(value[5])
        ht = Httpconfig(url,month,params)
        re = ht.http()
        errorCode = re[0]["errorCode"]   #获取返回值的errorCode的值，实际结果
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
            print("执行完毕")
        # 断言预期结果与实际结果是否一致
        self.assertEqual(expected_results, errorCode, msg="用例失败")
    @data(*excle_data_add)
    def test_add(self,value):
        ht = Httpconfig()
        url = value[3]
        month = value[4]
        params = eval(value[5])
        if value[10] != " ":
            coo = ht.login()   #请求登录接口获取到cookie值
            ht = Httpconfig(url,month,params,coo)
            re = ht.http()
            title = re[0]["data"]["title"] # 获取返回值的title的值，实际结果
            status_code = re[1]  # 获取响应状态码
            expected_results = value[6] # 获取测试用例中预期结果的值
            id = int(value[0])  # 获取测试用例的id
            errorMsg = re[0]["errorMsg"].encode("utf-8")    # 获取返回值的errorMsg的值，
            errorMsg1 = re[0]["errorMsg"]
            # if errorMsg != " ":
            #     if expected_results == errorMsg:
            #         wr = Writeexcle(id, 7, errorMsg1)
            #         wr.rewrite()
            #         wr = Writeexcle(id, 8, status_code)
            #         wr.rewrite()
            #         wr = Writeexcle(id, 9, "pass")
            #         wr.rewrite()
            #     elif expected_results != errorMsg:
            #         wr = Writeexcle(id, 7, errorMsg1)
            #         wr.rewrite()
            #         wr = Writeexcle(id, 8, status_code)
            #         wr.rewrite()
            #         wr = Writeexcle(id, 9, "fail")
            #         wr.rewrite()
            #     self.assertEqual(expected_results, errorMsg, msg="用例失败")
            if True:
                try:
                    if expected_results == title:
                        wr = Writeexcle(id, 7, title)
                        wr.rewrite()
                        wr = Writeexcle(id, 8, status_code)
                        wr.rewrite()
                        wr = Writeexcle(id, 9, "pass")
                        wr.rewrite()
                    elif expected_results != title:
                        wr = Writeexcle(id, 7, title)
                        wr.rewrite()
                        wr = Writeexcle(id, 8, status_code)
                        wr.rewrite()
                        wr = Writeexcle(id, 9, "fail")
                        wr.rewrite()
                except Exception as msg:
                    print(f"报错信息为{msg}")
                else:
                    print("写入表格成功")
                finally:
                    print("执行完毕")
                # 断言预期结果与实际结果是否一致
                self.assertEqual(expected_results, title, msg="用例失败")
        else:
            pass   #用例按照功能分的sheet，若是有前置条件需要登录，则执行else部分，后续补充
    def tearDown(self):
        print("每条测试用例结束")
    @classmethod
    def tearDownClass(cls):
        print("测试结束")
unittest.main
# if __name__ == '__main__':
#     unittest.main()
