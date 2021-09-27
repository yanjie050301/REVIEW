"""
 -*- coding: utf-8 -*-
 @File  : apilianxi.py
 @Author: yanjie
 @Date  : 2021/9/26 0026
 @功能描述  :
 @实现步骤：
    1.
    2.
    3.
"""
import requests,json
he = {


}
u = "https://www.wanandroid.com/user/login"
param = {
    "username":"yanjie000",
    "password":"123123"
}

re = requests.post(url=u,data=param)
print(re.json())
name =re.json()["data"]["nickname"]
print(name)

