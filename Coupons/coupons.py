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
@操作说明：
    1、header里的authorization字段值要与删除redis的用户信息一致
    2、删除redis的key值直接复制redis中的，或者询问开发
"""
import requests,json,redis
class Coupons():
    def connection_resid(self,environment):
        # 连接redis
        if environment == "exe":
            self.rexe = redis.Redis(host="r-2zel7jhfxuulhcytl3.redis.rds.aliyuncs.com", port=6379, db=4,
                             password="Rfy2ymvb3%BzfMu#", encoding="utf-8")
            return self.rexe
        elif environment == "mega":
            self.rmega = redis.Redis(host="10.110.203.201", port=6379, db=1,
                             password="z9SdeWy8aiZgqGX2", encoding="utf-8")
            return self.rmega
    def delete_key(self,environment,keys):
        r = self.connection_resid(environment)
        result = r.delete(keys)
        return result
    def mega_coupons(self,activity_key):
        # 获取折扣详细信息接口
        url = "https://boxonline-experience.paquapp.com/popactivity/v1/activity_voteDiscount/vote?key="+activity_key #后面拼接的活动key
        data = {
            "id": "23",   #投票的精灵id
            "ts": "1639638017207",
            "sign": "7754D1B26CFB9BA8F097161B287C5F16"
        }
        # mega环境的header
        header = {
            "content-type": "application/x-www-form-urlencoded",
            "Host": "megaboxonline.paquapp.com",
            "X-Project-ID": "boxonline",
            "X-Sign": "b252ba2ec89d1dea90adf06ca1200f78,1639631793203",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJveG9ubGluZSJ9.eyJnaWQiOiI3ODgiLCJuaWNrbmFtZSI6IumXq-a0geWwj-WPtyIsImF2YXRhciI6Imh0dHBzOi8vdGhpcmR3eC5xbG9nby5jbi9tbW9wZW4vdmlfMzIvSVhHM3BQWkRCRzBpYWJ4bmpIaWIzSUFjSkV3V2x6ODdtU0xXN3YwYmFpYmVNQ2JqdWsxcURrOU01a2VWYXZ6QnNpYjQ5NmM5UmliYkJ3YlBiMW1ER0ZQaWNZeUEvMTMyIiwidmlwTGV2ZWwiOjAsInJvbGUiOiJVc2VyIiwiYXBwSUQiOjMsImFwcENvZGUiOjAsInByb3ZpZGVyVHlwZSI6IndlY2hhdCIsImxvZ2luQXQiOjE2Mzk3Mjk5MDAsInNob3dJRCI6IjM5OTExNzkyNzgzOTYyNDgxNTcyNTUiLCJwcm9qZWN0SWQiOiJib3hvbmxpbmUiLCJwcm92aWRlcklEIjoiIiwicHJvdmlkZXIiOiIiLCJvcGVuX2lkIjoib2hoUWY1Y0NZR2N0OENTSTRJaThBQVBIelpybyIsInVuaW9uX2lkIjoib3h5MzV3VmNqWkJDRU5TQ3Q0UEpuci1faWc4VSIsInNlc3Npb25fa2V5IjoienpUb1Y1WHBBakcyeUEvQ2lNM2lFUT09IiwicmVnaXN0ZXJBdCI6IjIwMjEtMTItMTZUMDY6MDE6NTAuMDAwWiIsImxhc3RMb2dpblRpbWUiOiIiLCJpc1BheVVzZXIiOmZhbHNlLCJwbGF5ZXJfaWQiOjY3Njg5ODksInN1YiI6Im94eTM1d1ZjalpCQ0VOU0N0NFBKbnItX2lnOFUiLCJwb3B2aXBfbGV2ZWwiOjEsInJvbGVzIjoiVVNFUiIsInVpZCI6IjY3Njg5ODkiLCJpYXQiOjE2Mzk3Mjk5MDAsImV4cCI6MTYzOTc3MzEwMH0.WKlagS9h0-2MBHBPEqL3nX5PCoVkkSWzfFEdXPRBcg4"
        }
        return url,data,header
    def exe_coupons(self,activity_key):
        #获取折扣详细信息
        url = "https://boxonline-experience.paquapp.com/popactivity/v1/activity_voteDiscount/vote?key="+activity_key #后面拼接的活动key
        #参数
        data = {
            "id":"23",
            "ts":"1639638017207",
            "sign":"7754D1B26CFB9BA8F097161B287C5F16"
        }

        #演练环境的header
        header = {
            "content-type":"application/x-www-form-urlencoded",
            "Host":"boxonline-experience.paquapp.com",
            "X-Project-ID": "boxonline",
            "X-Sign": "14215790c0a0de0176f04d9a8acb86a4,1639638017197",
            "authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJveG9ubGluZSJ9.eyJnaWQiOiI3ODgiLCJuaWNrbmFtZSI6IumXq-a0geWwj-WPtyIsImF2YXRhciI6Imh0dHBzOi8vdGhpcmR3eC5xbG9nby5jbi9tbW9wZW4vdmlfMzIvSVhHM3BQWkRCRzBpYWJ4bmpIaWIzSUFjSkV3V2x6ODdtU0xXN3YwYmFpYmVNQ2JqdWsxcURrOU01a2VWYXZ6QnNpYjQ5NmM5UmliYkJ3YlBiMW1ER0ZQaWNZeUEvMTMyIiwidmlwTGV2ZWwiOjAsInJvbGUiOiJVc2VyIiwiYXBwSUQiOjMsImFwcENvZGUiOjAsInByb3ZpZGVyVHlwZSI6IndlY2hhdCIsImxvZ2luQXQiOjE2Mzk2NDM5NjksInNob3dJRCI6IjM5OTExNzkyNzgzOTYyNDgxNTcyNTUiLCJwcm9qZWN0SWQiOiJib3hvbmxpbmUiLCJwcm92aWRlcklEIjoiIiwicHJvdmlkZXIiOiIiLCJvcGVuX2lkIjoib2hoUWY1Y0NZR2N0OENTSTRJaThBQVBIelpybyIsInVuaW9uX2lkIjoib3h5MzV3VmNqWkJDRU5TQ3Q0UEpuci1faWc4VSIsInNlc3Npb25fa2V5IjoiYWhOMlg1cGhnQXZ5R0lIUENOQ2ZXdz09IiwicmVnaXN0ZXJBdCI6IjIwMjEtMTItMTZUMDc6MDY6NTIuMDAwWiIsImxhc3RMb2dpblRpbWUiOiIiLCJpc1BheVVzZXIiOnRydWUsInBsYXllcl9pZCI6ODQzODU2OCwic3ViIjoib3h5MzV3VmNqWkJDRU5TQ3Q0UEpuci1faWc4VSIsInBvcHZpcF9sZXZlbCI6MSwicm9sZXMiOiJVU0VSIiwidWlkIjoiODQzODU2OCIsImlhdCI6MTYzOTY0Mzk2OSwiZXhwIjoxNjM5Njg3MTY5fQ.KnRYmfX_vyHfE2GnzwrRNdGGMNI47cdM5e8Q51aK4BM"
        }
        return url, data, header
    def run(self,environment,keys,keys1,activity_key):
        #初始化用户获取折扣券数量
        num5,num6,num7,num8,num9 = 0,0,0,0,0
        if environment =="mega":
            list_data = self.mega_coupons(activity_key)
        elif environment =="exe":
            list_data = self.exe_coupons(activity_key)
        else:
            print("请输入正确的测试环境值！exe or mega")
        # print(list_data)
        url = list_data[0]
        data = list_data[1]
        header = list_data[2]
        for b in range(1):
            for a in range(10):
                r = requests.post(url=url, data=data, headers=header)
                print(r.json(),end="")
                try:
                    discountValue = r.json()['data']['discountValue']  # 获取优惠券折扣值
                    self.delete_key(environment,keys)  #删除Redis的对应的key值
                    self.delete_key(environment,keys1)
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
                except  Exception as msg:
                    print(msg)
                finally:
                    print("")
        print(f"五折券:",{num5},"六折券:",{num6},"七折券:",{num7},"八折券:",{num8},"九折券:",{num9})
if __name__ == '__main__':
    c = Coupons()
    #删除Redis的key值
    keys = "activity:voteDiscount:voteDiscount_20211214a:day:1:voteId:6768989"  #voteDiscount_20211216:活动key，day:1 活动第几天；voteId:8437916 投票的用户id
    keys1 = "activity:voteDiscount:voteDiscount_20211214a:day:1:discountValue:6768989"
    #活动key值
    activity_key = "voteDiscount_20211214a"
    c.run("mega",keys,keys1,activity_key)
