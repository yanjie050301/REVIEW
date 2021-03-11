"""
功能描述：
1.调用readExcel模块，读取册数数据
2.根据测试数据中每个接口的请求方式，进行对应的请求

"""



"""
[{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'zhuxiaodong','password':'test01'}", 'expect': '0', 'real': '', 'status': ''},
 {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'zxd01','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''}, 
 {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'Get', 'value': "{'username':'zhuxiaodong'}", 'expect': '0', 'real': '', 'status': ''}]
"""
"""
*************************************************最初的代码***********
"""
"""
import unittest
import requests,json
from common.readexcel import ReadExcel
from common.HttpConfig import Httpconfig
from ddt import ddt,data,unpack
class TestCase(unittest.TestCase):
    #1.初始化方法
    @classmethod              #@classmethod作用，可以看做是静态类，可以传进来一个当前类作为第一个参数，去传给当前类作用于该类下面的方法
    def setUpClass(cls):         #所有用例之前执行，所有测试用例前的设置工作，初始化环境
        print("测试开始")
        #1.调用ReadExcel模块，读取测试数据
        read_excel = ReadExcel()
        cls.read_data = read_excel.read_exc()
    def setUp(self):           #每条用例之前执行，每条测试用例前的设置工作，初始化环境
        pass
    def test_case(self):
        #提取测试数据
            interfaceUrl = self.read_data[0]["interfaceUrl"]   #测试的url
            Method = self.read_data[0]["Method"]     #测试的请求方法
            values = self.read_data[0]["value"]     #测试数据,获取的值是str类型
            expect = self.read_data[0]["expect"]     #预期结果
            print(values)
            # global r
            if Method.lower() == "get":
                r = requests.get(url= interfaceUrl,params= values)
            elif Method.lower() == "post":
                r = requests.post(url= interfaceUrl,data= eval(values))        #eval()函数，将获取出来的str类型，转化为字典类型
            else:
                pass
            errorCode = r.json()["errorCode"]
            self.assertEqual(errorCode,int(expect),msg = "测试结果为fail")
    def tearDown(self):        #每条用例执行完之后执行，每条测试用例执行后的清洗工作，还原环境
        pass
    @classmethod
    def tearDownClass(cls):        #所有用例执行完之后执行，所有测试用例执行后的清洗工作，还原环境
        print("测试结束")

if __name__ == '__main__':
    unittest.main()
"""
"""
*************************************************优化的代码***********将测试数据和请求方法再次封装，是代码变得简洁
"""
"""
import unittest
from common.readexcel import ReadExcel
from common.HttpConfig import Httpconfig
from ddt import ddt,data,unpack
#初始化ReadExcel
read_excel = ReadExcel()
#从excel中获取测试数据，
read_data = read_excel.read_exc()      #获取出来的是一个以字典为元素的列表
@ddt  #ddt框架要结合unittest框架进行使用，必须放在类的前面
class TextCase(unittest.TestCase):
    #使用装饰器,作用：将该方法作为参数传给另一个方法
    @classmethod
    def setUpClass(cls):
        print("整体测试开始，准备环境")
    def setUp(self):
        print("每条测试开始，准备环境")
    @data(*read_data)     #使用@data修饰器，实现依次读取数据，写法列表前面必须用*，传可变长参数，若是键值对前面必须用**，传关键字参数
    def test_case(self,value):
        # print("11111",value)
        # 初始化Httpconfig
        hc = Httpconfig(**value)        #可变长参数，传值的时候也要带**，传关键字参数
        real = hc.http()
        # print("2222222",real)
        # print("2222",type(real))
        # print("1111",type(value["expect"]))
        #添加断言
        expect = int(value["expect"])        #except取出来的是str类型，而real是int类型，要保持一致才可进行断言
        try:
            self.assertEqual(real,expect,msg=f"实际结果为{real}，预期结果为{expect},测试执行失败")
        except Exception as msg:
            print(msg)
        finally:
            print("用例执行完毕")
    def tearDown(self):
        print("每条测试结束，还原环境")
    @classmethod
    def tearDownClass(cls):
        print("总体测试结束，还原环境")
if __name__ == '__main__':
    unittest.main()
"""
"""
*************************************************优化的代码***********请求接口的结果，将接口状态和errorcode码写入excel中
"""
import unittest
from common.readexcel import ReadExcel
from common.HttpConfig import Httpconfig
from ddt import ddt,data,unpack
from common.writeexcel import WriteExcel
from common.logconfig import log
#初始化ReadExcel
read_excel = ReadExcel()
#从excel中获取测试数据，
read_data = read_excel.read_exc()      #获取出来的是一个以字典为元素的列表
logger = log()
@ddt  #ddt框架要结合unittest框架进行使用，必须放在类的前面
class TextCase(unittest.TestCase):
    #使用装饰器,作用：将该方法作为参数传给另一个方法
    @classmethod
    def setUpClass(cls):
        print("整体测试开始，准备环境")
    def setUp(self):
        print("每条测试开始，准备环境")
    @data(*read_data)     #使用@data修饰器，实现依次读取数据，写法列表前面必须用*，传可变长参数，若是键值对前面必须用**，传关键字参数
    def test_case(self,value):
        # print("11111",value)
        # 初始化Httpconfig
        hc = Httpconfig(**value)        #可变长参数，传值的时候也要带**，传关键字参数
        http_result = hc.http()
        # print(type(http_result))
        real = http_result[0]
        status = http_result[1]
        #添加断言
        expect = int(value["expect"])        #except取出来的是str类型，而real是int类型，要保持一致才可进行断言
        try:
            self.assertEqual(real,expect,msg=f"实际结果为{real}，预期结果为{expect},测试执行失败")
        except Exception as msg:
            logger.info(msg)
        finally:
            logger.info("用例执行完毕")
        id = int(value["id"])                   #获取excel表格中id的值，并把它转化为int类型
        #初始化WriteExcel
        we = WriteExcel(id,real,status)
        #将请求结果的相关数据，写入表格中，errorCode和status_code的值，分别对应表格中的real和status字段
        we.save_e()
    def tearDown(self):
        print("每条测试结束，还原环境")
    @classmethod
    def tearDownClass(cls):
        print("总体测试结束，还原环境")
if __name__ == '__main__':
    unittest.main()