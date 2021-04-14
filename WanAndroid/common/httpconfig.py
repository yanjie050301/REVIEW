"""
功能介绍：再次封装request方法，实现传出什么参数，就调用哪个方法

"""
import requests,json
class Httpconfig():
    def __init__(self,url,method,data = None,coo = None):
        self.url = url
        self.data = data
        self.method = method
        self.coo = coo
    def login(self):
        re = requests.post(url=self.url, data=self.data)
        return re.cookies
    def get(self):
        re = requests.get(url= self.url,params = self.data,cookies = self.coo)
        return re.json()
    def post(self):
        re = requests.post(url= self.url,data = self.data,cookies = self.coo)
        return re.json()
    def http(self):
        if self.method == "post":
            self.post()
        elif self.method == "get":
            self.get()
        else:
            return "请求方法错误"
if __name__ == '__main__':
    url = "https://www.wanandroid.com/user/login"
    data = {"username": "yanjie000", "password": "123123"}
    url1 = "https://www.wanandroid.com/lg/todo/list/1"
    url2 = "https://www.wanandroid.com/user/logout/json"
    a = Httpconfig(url,"post",data)
    print(a.login())
    # coo = r.cookies