import requests,json,time
import chardet
url = "https://www.wanandroid.com/user/login"
data = {"username":"yanjie000","password":"123123"}
# r = requests.session()
r1 = requests.post(url=url,data=data)
coo = r1.cookies
q = "https://www.wanandroid.com/lg/todo/done/25859/json"
r2 = requests.post(url=q,cookies=coo)
print(r2.text)