import requests,json

url = "https://www.wanandroid.com/user/login"
data = {"username":"yanjie000","password":"123123"}
r = requests.session()
r1 = r.post(url=url,data=data)
print("登录接口",r1.json())


# url1 = "https://www.wanandroid.com/lg/todo/add/json"
# data1 = {"title":"dd","content":"ddddd","date":"","type":8}
# r2 = r.post(url=url1,data=data1)
# # print("添加清单接口",r2.text)
#
# url1 = "https://www.wanandroid.com/lg/todo/list/1"
# r3 = r.get(url=url1)
# # print("获取清单列表",r3.text)

# url2 = "https://www.wanandroid.com/lg/todo/delete/25701/json"
# r4 = r.post(url=url2)
# print("删除清单",r4.text)

# url2 = "https://www.wanandroid.com/lg/todo/done/25705/json"
# r4 = r.post(url=url2)
# print("完成清单",r4.text)