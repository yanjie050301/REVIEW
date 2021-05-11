"""
功能介绍：
1.添加完成待办清单列表接口
"""
import readexcle,json,ddt,data,unittest
from WanAndroid.common.readexcle import Readexcle
from WanAndroid.common.writeexcle import Writeexcle
from WanAndroid.common.httpconfig import Httpconfig
data_com = Readexcle("完成待办清单")
datas_com = data_com.getdata()  #从excle获取完成待办清单的数据
@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试环境开始")
    def setUp(self):
        print("用例环境开始")
    @data(*datas_com)
    def test_com(self,values):
        uid = str(int((values[3])))  # 从表格中获取id值为float，需要转化为int类型在转化为string类型，方便后面url的拼接
        u = values[4]
        url = u + uid + "/json"  # 拼接好的url
        method = values[5]
        ht = Httpconfig()
        coo = ht.login()  # 获取用户登录的cookie
        re = Httpconfig(url, method, cookies=coo)
        r = re.http()
        status = r[1]  # 获取接口请求状态
        # eval无法解析null， true， false之类的数据
        global false, null, true
        false = null = true = ''
        r_json = eval(r[0])  # 获取服务器返回的数据，类型为dict
        actual_results = r_json.get("errorCode")  # 获取服务器返回的错误码
        id = values[0]  # 获取表格id
        expected_results = int(values[7])  # 获取预期结果




    def tearDown(self):
        print("用例环境结束")
    @classmethod
    def tearDownClass(cls):
        print("测试环境结束")