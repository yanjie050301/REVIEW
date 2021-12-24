"""
 -*- coding: utf-8 -*-
 @File  : yamlxl.py
 @Author: yanjie
 @Date  : 2021/12/8 11:29 上午
 @功能描述  :yaml数据化读取练习
 @实现步骤：
    1.创建yaml对象
    2.读取yaml格式文件
"""
from ruamel.yaml import YAML
import requests,json
#1.创建yaml对象
yaml = YAML(typ="safe")
#2.读取yaml格式文件
with open ("lianxi.yaml",encoding="utf-8") as file:
    data1 = yaml.load(file)
print(data1)

url = "https://www.wanandroid.com/user/login"
data = {
    "username": data1["username"],
    "password": data1["password"]
}
r = requests.post(url=url,data=data)
print(r.text)




