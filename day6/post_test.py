import requests
import json

"""
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
# 接口文档要求以json格式传参
# 方法一：dumps转换
datas = json.dumps(datas)
# 方法二：
r = requests.post(url= urlstr,data= datas)
# 3.输出响应数据
# print(r.status_code)
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

#session练习   .通过session函数自动携带上次请求返回的cookie信息，发送二次post请求
"""
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
"""

#练习查快递的接口









# 携带cookie发送请求
"""
###########方法一##############通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie
# 1.请求地址
urlstr = "https://wanandroid.com/user/login"
# 2.发送请求
datas = {"username":"yanjie000","password":"123123"}
r = requests.post(url=urlstr,data=datas)
print("********",r.cookies)
print("**",r.headers)
# 获取cookie值传给下一个请求
cookie = r.cookies
print("555",cookie)
r2 = requests.get("https://wanandroid.com/1g/todo/list/0",cookies = cookie)
print(r2.status_code)
"""
###########方法二##############通过requests.session自动设置cookie，来完成访问





###########方法三##############通过定制cookie，单独设置cookie来访问目标网址






###########方法四##############通过定制cookie，放入header来访问目标网址











































