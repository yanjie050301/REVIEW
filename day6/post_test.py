import requests
import json

"""
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
# datas = {"username":"yanjie000","password":"123123"}
datas = {'username':'zhuxiaodong','password':'test01'}
print(type(datas))
r = requests.post(url= urlstr,data = datas)
# 3.输出响应数据
print(r.status_code)
print(r.text)
#响应结果为res_result
res_result = r.json()
# 响应结果中提取errorCode的值
errorCode = res_result["errorCode"]
# 响应结果中提取username的值
username = res_result["data"]["username"]
#响应断言
if errorCode == 0 and username == datas.get("username"):
    print("登陆成功")
"""

############json传参练习
# post请求，传参方式是以json格式传参
"""
#方法一，先导入json模块，用dumps方法转化成json格式
urlstr = 'http://httpbin.org/post'
payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
#通过json.dumps方式将python字符串转化为json类型
# payload = json.dumps(payload)
# r = requests.post(url= urlstr,data = payload)
# print(r.text)
#方法二，使用json参数默认处理成json格式进行传递
r = requests.post(url= urlstr,json = payload)
print(r.text)
# print(r.json())
"""


#session练习   .通过session函数自动携带上次请求返回的cookie信息，发送二次post请求

# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
se = requests.session()
r = se.post(url= urlstr,data= datas)
r2 = se.get("https://wanandroid.com/1g/todo/list/0")
#不加session的话，请求接口会显示让先登录
# r2 = requests.get("https://wanandroid.com/1g/todo/list/0")
# 3.输出响应数据
print(r2.text)


#练习查快递的接口
#####################打开快递网：http://www.kuaidi.com/，搜索某个单号，判断它的状态是不是已签收
"""
url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-UUCAO1613872252544.html"
herders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
          }
s = requests.session()
re = s.post(url = url)
res = re.json()
print(res)
data = res["data"][0]["context"]
# print(data)
if "包裹已签收"in data:
    print("包裹已签收")
else:
    print("包裹未签收")

"""
# 携带cookie发送请求

###########方法一##############通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie
"""
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
r = requests.post(url=urlstr,data=datas)
#手动获取上一个请求的cookies
coo = r.cookies
url1 = "https://www.wanandroid.com/lg/todo/list/0"
#带入下一个请求中，进行提交
r1 = requests.get(url = url1,cookies =coo)
print(r1.text,r1.status_code)
"""
###########方法二##############通过requests.session自动设置cookie，来完成访问
"""
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
#初始化session对象
s = requests.session()
#通过session对象发送请求，服务器设置在本地的cookie会自动保存到本地
r = s.post(url=urlstr,data=datas)
#带入下一个请求中，进行提交
url1 = "https://www.wanandroid.com/lg/todo/list/0"
r1 = s.get(url = url1)
print(r1.status_code)
"""
###########方法三##############通过定制cookie，单独设置cookie来访问目标网址
"""
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
r = requests.post(url = urlstr,data= datas)
print(r.cookies)
#手动获取到cookies返回的JSESSIONID
coo = r.cookies["JSESSIONID"]
#通过字典的形式引用cookies返回的JSESSIONID，放入下次请求的cookies中
cooki = {
    'cookies' : coo
}
url1 = "https://www.wanandroid.com/lg/todo/list/0"
r1 = requests.get(url= url1,cookies = cooki)
print(r1.status_code)
"""
###########方法四##############通过定制cookie，放入header来访问目标网址
"""
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
r = requests.post(url = urlstr,data= datas)
#手动获取cookies返回的JSESSIONID
coo = r.cookies["JSESSIONID"]
#通过字典的形式引用cookies返回的JSESSIONID，放入下次请求的headers中
herder = {
    "cookie":"JSESSIONID="+coo   #通过拼接形式将JSESSIONID = A2751057CAC77A085A4FF25A55EE7D2C拼接起来
}
url1 = "https://www.wanandroid.com/lg/todo/list/0"
r1 = requests.get(url= url1,headers = herder)
print(r1.status_code)
"""







































