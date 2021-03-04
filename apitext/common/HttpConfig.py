"""
功能说明：
1.将测试数据再次整理封装
2.二次封装请求方式


"""
import requests
class Httpconfig():
    def __init__(self,**kwargs):        #kwargs用作传递键值可变长参数列表，它是一个dict
        #获取传入列表的值
        self.interfaceUrl = kwargs["interfaceUrl"]     # 测试的url
        self.Method = kwargs["Method"]  # 测试的请求方法
        self.values = kwargs["value"]  # 测试数据,获取的值是str类型
        self.expect = kwargs["expect"]  # 预期结果
        # print(self.interfaceUrl)
    def http(self):
        #根据Method值的请求类型，调用对用的请求方式
        if self.Method.lower() == "get":
            return self.get()
        elif self.Method.lower() == "post":
            return self.post()
        else:
            return "请求方法错误"
    def get(self):   #二次封装的get方法和post方法
        r = requests.get(url=self.interfaceUrl,params=eval(self.values))        #eval()函数，将获取出来的str类型，转化为字典类型
        return r.json()["errorCode"]
    def post(self):
        r = requests.post(url=self.interfaceUrl,data=eval(self.values))
        return r.json()["errorCode"]
if __name__ == '__main__':
    data = [{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'zhuxiaodong','password':'test01'}", 'expect': '0', 'real': '', 'status': ''},
 {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'zxd01','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''},
 {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'Get', 'value': "{'username':'zhuxiaodong'}", 'expect': '0', 'real': '', 'status': ''}]
    a = Httpconfig(**data[0])        #可变长参数，传值的时候也要带**，传关键字参数
    print(a.http())