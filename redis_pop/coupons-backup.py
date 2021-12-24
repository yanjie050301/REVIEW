"""
 -*- coding: utf-8 -*-
 @File  : coupons.py
 @Author: yanjie
 @Date  : 2021/12/8 5:31 下午
 @功能描述  :测试守护精灵投票优惠券权重
 @实现步骤：
    1.导包Redis,实例化
    2.调通获取优惠券接口
    3.循环调用接口，每次调用之后，删除Redis相应的key值
"""
from read_redis import Rsdis
import requests,json,time
#获取折扣详细信息
url = "https://boxonline-experience.paquapp.com/popactivity/v1/activity_voteDiscount/vote?key=voteDiscount_20211216"
#参数
data = {
    "id":"24",
    "ts":"1639638017207",
    "sign":"7754D1B26CFB9BA8F097161B287C5F16"
}
#mega环境的header
header1 = {
    "content-type":"application/x-www-form-urlencoded",
    "Host":"megaboxonline.paquapp.com",
    "X-Project-ID": "boxonline",
    "X-Sign": "b252ba2ec89d1dea90adf06ca1200f78,1639631793203",
    "authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJveG9ubGluZSJ9.eyJnaWQiOiI3ODgiLCJuaWNrbmFtZSI6IumXq-a0geWwj-WPtyIsImF2YXRhciI6Imh0dHBzOi8vdGhpcmR3eC5xbG9nby5jbi9tbW9wZW4vdmlfMzIvSVhHM3BQWkRCRzBpYWJ4bmpIaWIzSUFjSkV3V2x6ODdtU0xXN3YwYmFpYmVNQ2JqdWsxcURrOU01a2VWYXZ6QnNpYjQ5NmM5UmliYkJ3YlBiMW1ER0ZQaWNZeUEvMTMyIiwidmlwTGV2ZWwiOjAsInJvbGUiOiJVc2VyIiwiYXBwSUQiOjMsImFwcENvZGUiOjAsInByb3ZpZGVyVHlwZSI6IndlY2hhdCIsImxvZ2luQXQiOjE2Mzk2MzQ1MjcsInNob3dJRCI6IjM5OTExNzkyNzgzOTYyNDgxNTcyNTUiLCJwcm9qZWN0SWQiOiJib3hvbmxpbmUiLCJwcm92aWRlcklEIjoiIiwicHJvdmlkZXIiOiIiLCJvcGVuX2lkIjoib2hoUWY1Y0NZR2N0OENTSTRJaThBQVBIelpybyIsInVuaW9uX2lkIjoib3h5MzV3VmNqWkJDRU5TQ3Q0UEpuci1faWc4VSIsInNlc3Npb25fa2V5IjoiUXhqeGtQb2hKT3FPYVd1TWN1OEFDQT09IiwicmVnaXN0ZXJBdCI6IjIwMjEtMTItMTZUMDY6MDE6NTAuMDAwWiIsImxhc3RMb2dpblRpbWUiOiIiLCJpc1BheVVzZXIiOmZhbHNlLCJwbGF5ZXJfaWQiOjY3Njg5ODksInN1YiI6Im94eTM1d1ZjalpCQ0VOU0N0NFBKbnItX2lnOFUiLCJwb3B2aXBfbGV2ZWwiOjEsInJvbGVzIjoiVVNFUiIsInVpZCI6IjY3Njg5ODkiLCJpYXQiOjE2Mzk2MzQ1MjcsImV4cCI6MTYzOTY3NzcyN30.zUnRyomcmsTZfHzQAAiX1FmBCJrZA6r8iSsVBUTVEmY"
}
#演练环境的header
header = {
    "content-type":"application/x-www-form-urlencoded",
    "Host":"boxonline-experience.paquapp.com",
    "X-Project-ID": "boxonline",
    "X-Sign": "14215790c0a0de0176f04d9a8acb86a4,1639638017197",
    "authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJveG9ubGluZSJ9.eyJnaWQiOiI3ODgiLCJuaWNrbmFtZSI6IumXq-a0geWwj-WPtyIsImF2YXRhciI6Imh0dHBzOi8vdGhpcmR3eC5xbG9nby5jbi9tbW9wZW4vdmlfMzIvSVhHM3BQWkRCRzBpYWJ4bmpIaWIzSUFjSkV3V2x6ODdtU0xXN3YwYmFpYmVNQ2JqdWsxcURrOU01a2VWYXZ6QnNpYjQ5NmM5UmliYkJ3YlBiMW1ER0ZQaWNZeUEvMTMyIiwidmlwTGV2ZWwiOjAsInJvbGUiOiJVc2VyIiwiYXBwSUQiOjMsImFwcENvZGUiOjAsInByb3ZpZGVyVHlwZSI6IndlY2hhdCIsImxvZ2luQXQiOjE2Mzk2NDM5NjksInNob3dJRCI6IjM5OTExNzkyNzgzOTYyNDgxNTcyNTUiLCJwcm9qZWN0SWQiOiJib3hvbmxpbmUiLCJwcm92aWRlcklEIjoiIiwicHJvdmlkZXIiOiIiLCJvcGVuX2lkIjoib2hoUWY1Y0NZR2N0OENTSTRJaThBQVBIelpybyIsInVuaW9uX2lkIjoib3h5MzV3VmNqWkJDRU5TQ3Q0UEpuci1faWc4VSIsInNlc3Npb25fa2V5IjoiYWhOMlg1cGhnQXZ5R0lIUENOQ2ZXdz09IiwicmVnaXN0ZXJBdCI6IjIwMjEtMTItMTZUMDc6MDY6NTIuMDAwWiIsImxhc3RMb2dpblRpbWUiOiIiLCJpc1BheVVzZXIiOnRydWUsInBsYXllcl9pZCI6ODQzODU2OCwic3ViIjoib3h5MzV3VmNqWkJDRU5TQ3Q0UEpuci1faWc4VSIsInBvcHZpcF9sZXZlbCI6MSwicm9sZXMiOiJVU0VSIiwidWlkIjoiODQzODU2OCIsImlhdCI6MTYzOTY0Mzk2OSwiZXhwIjoxNjM5Njg3MTY5fQ.KnRYmfX_vyHfE2GnzwrRNdGGMNI47cdM5e8Q51aK4BM"
}
num5,num6,num7,num8,num9 = 0,0,0,0,0
re = Rsdis()
#删除Redis的key值
keys = "activity:voteDiscount:voteDiscount_20211216:day:1:voteId:8438568"
keys1 = "activity:voteDiscount:voteDiscount_20211216:day:1:discountValue:8438568"
#循环1000次查看领取优惠券权重
for b in range(10):
    for a in range(100):
        r = requests.post(url=url, data=data, headers=header)
        print(r.json())
        discountValue = r.json()['data']['discountValue']  # 获取优惠券折扣值
        re.delete_key(keys)  #删除Redis的对应的key值
        re.delete_key(keys1)
        if discountValue == 5:
            num5 = num5+1
        elif discountValue == 6:
            num6 = num6 + 1
        elif discountValue == 7:
            num7 = num7 + 1
        elif discountValue == 8:
            num8 = num8 + 1
        elif discountValue == 9:
            num9 = num9 + 1
print(f"五折券:",{num5},"六折券:",{num6},"七折券:",{num7},"八折券:",{num8},"九折券:",{num9})
