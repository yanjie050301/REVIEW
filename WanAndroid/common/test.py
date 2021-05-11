import requests,json,time
import chardet
url = "https://www.wanandroid.com/user/login"
data = {"username":"yanjie000","password":"123123"}
r = requests.session()
r1 = r.post(url=url,data=data)
# r = requests.post(url=url,data=data)
# print("登录接口",r1.json())
# coo = r1.cookies["JSESSIONID"]
# coo = r.cookies
# print(coo)
# cook ={
#     "cookie" : coo
# }
# header = {
#     "cookie":"JSESSIONID="+coo
# }
# time.sleep(5)
# url1 = "https://www.wanandroid.com/lg/todo/add/json"
# data1 = {"title":"ceshi0000","content":"ddddd","date":"2021-03-31","type":0}
# data2 = {"title":"","content":"ddddd","date":"2021-03-31","type":0}
# # r2 = requests.post(url=url1,data=data1,headers=header)
# r1 = requests.post(url=url1,data=data1,cookies=coo)
# r2 = requests.post(url=url1,data=data2,cookies=coo)
# r2 = r2.json()
# word = r2["errorMsg"].encode("utf-8")
# li = [11.0, '添加待办清单', '添加的数据标题为空', 'https://www.wanandroid.com/lg/todo/add/json', 'post', '{"title":"","content":"ddddd","date":"2021-03-31","type":0}', '标题不能为空！', '', '', '', 'cookies', '验证errorMsg字段值']
# errorMsg = li[6].encode("utf-8")
# # print(errorMsg)
# assert(word !=errorMsg)
#
# string_code = chardet.detect(errorMsg)
# print(string_code)
# url1 = "https://www.wanandroid.com/lg/todo/list/1"
# r3 = requests.get(url=url1,cookies = coo)
# print("获取清单列表",r3.text)

# url2 = "https://www.wanandroid.com/lg/todo/delete/25701/json"
# r4 = r.post(url=url2)
# print("删除清单",r4.text)

url2 = "https://www.wanandroid.com/lg/todo/done/26112/json"
r4 = r.post(url=url2)
print("完成清单",r4.text)

# url5 = "https://www.wanandroid.com/lg/todo/done/25856/json"
# status="1"
# r5 = r.post(url= url5,data=status)
# print(r5.text)
# print (time.strftime("%Y-%m-%d"))