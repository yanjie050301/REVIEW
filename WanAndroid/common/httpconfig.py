"""
功能介绍：再次封装request方法，实现传出什么参数，就调用哪个方法

"""
import requests,json
class Httpconfig():
    def __init__(self,url= None,method= None,data = None,cookies= None):
        self.url = url
        self.data = data
        self.method = method
        self.cookies = cookies
    def login(self):   #为后面的接口提供cookie
        lo = requests.post(url="https://www.wanandroid.com/user/login", data={"username": "yanjie000", "password": "123123"})
        return lo.cookies
    def get(self):
        re = requests.get(url= self.url,params = self.data,cookies= self.cookies)
        return re.json(),re.status_code
    def post(self):
        re = requests.post(url= self.url,data = self.data,cookies= self.cookies)
        return re.json(),re.status_code
    def http(self):
        if self.method == "post":
            return self.post()
        elif self.method == "get":
            return self.get()
        else:
            return "请求方法错误"
if __name__ == '__main__':
    url = "https://www.wanandroid.com/user/login"
    data = {"username": "yanjie000", "password": "123123"}
    url1 = "https://www.wanandroid.com/lg/todo/list/1"
    url2 = "https://www.wanandroid.com/lg/todo/add/json"
    data2 = {"title":"ceshi0000","content":"ddddd","date":"2021-03-31","type":0}
    method = "post"
    a = Httpconfig(url,method,data)
    # a = Httpconfig()
    # b = a.login()
    # print("555555555",b)
    # c = Httpconfig(url=url2,method="post",data=data2,cookies=b)
    d = a.http()
    print(d)