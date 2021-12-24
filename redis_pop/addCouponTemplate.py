"""
 -*- coding: utf-8 -*-
 @File  : addCouponTemplate.py
 @Author: yanjie
 @Date  : 2021/12/12 2:58 下午
 @功能描述  :新增优惠券
 @实现步骤：
    1.
    2.
    3.
"""
import requests,json,time
class AddCouponTemplate():
    def megadata(self,data=None):
        urlmega = "http://megawxcms.impaqu.com/apis/coupon/addCouponTemplate"
        header = {
            "content-type": "application/json",
            "Host": "megawxcms.impaqu.com",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwibmljayI6ImFkbWluIiwidGVsIjpudWxsLCJyb2xlIjowLCJhdXRoIjoxLCJzdGF0ZSI6MCwidXNlcl9pZCI6MSwicm9sZXMiOiJBRE1JTiIsInVpZCI6IjEiLCJpYXQiOjE2MzkyMDc3NjYsImV4cCI6MTYzOTI5NDE2Nn0.jz-Kma9RkioBHIAY4Liy1eRKzpXUmMBryZxoSJ5LS7A"
        }
        data_shop = {
            "couponTemplate":
                {"type":7,
                 "group_type":1,
                 "name":"惊喜专场九折券",
                 "value":500,
                 "use_min_price":89900,
                 "start_time":"null",
                 "end_time":"2021-12-15 00:00:00",
                 "valid_day":0,
                 "series_ids":"",
                 "channel":1,
                 "icon_pic":"",
                 "left_angle":"",
                 "redirect_shop_id":208,
                 "redirect_goods_id":"null",
                 "comment":"",
                 "is_from_outer":1,
                 "expire_type":1,
                 "is_disabled":False
                 }
        }

        data_box ={"couponTemplate":{"type":6,"group_type":1,"name":"惊喜专场五折券","value":3400,"use_min_price":6900,"start_time":"null","end_time":"2021-12-15 00:00:00","valid_day":0,"series_ids":"","channel":1,"icon_pic":"","left_angle":"","redirect_shop_id":"null","redirect_goods_id":875,"comment":"","is_from_outer":1,"expire_type":1,"is_disabled":False}}
        # r = requests.post(url=urlmega, json=data_box, headers=header)
        # print(r.text)
        if data == "data_box":
            return urlmega, data_box,header
        elif data == "data_shop":
            return urlmega, data_shop,header
    def exedata(self,data=None):
        urlexe = "http://boxonline-experience-cms.paquapp.com/apis/coupon/addCouponTemplate"
        header = {
            "content-type": "application/json",
            "Host": "boxonline-experience-cms.paquapp.com",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwibmljayI6ImFkbWluIiwidGVsIjpudWxsLCJyb2xlIjowLCJhdXRoIjoxLCJzdGF0ZSI6MCwidXNlcl9pZCI6MSwicm9sZXMiOiJBRE1JTiIsInVpZCI6IjEiLCJpYXQiOjE2Mzk4OTcyOTcsImV4cCI6MTYzOTk4MzY5N30.XQfHe-iu_AUlWvX7A3VyP-LSL2EEupSEiv2F4fCae9M"
        }
        data_box ={"couponTemplate":{"type":6,"group_type":1,"name":"惊喜专场五折券","value":3400,"use_min_price":6900,"start_time":"null","end_time":"2021-12-16 23:59:59","valid_day":0,"series_ids":"1609","channel":1,"icon_pic":"","left_angle":"","redirect_shop_id":"null","redirect_goods_id":1082,"comment":"","is_from_outer":1,"expire_type":1,"is_disabled":False}}
        data_shop = {"couponTemplate":{"type":7,"group_type":1,"name":"惊喜专场五折券","value":44900,"use_min_price":89900,"start_time":"null","end_time":"null","valid_day":"1","series_ids":"1831","channel":1,"icon_pic":"","left_angle":"","redirect_shop_id":1368,"redirect_goods_id":"null","comment":"","is_from_outer":1,"expire_type":2,"is_disabled":False}}
        # r = requests.post(url=urlexe, json=data_box, headers=header)
        # print(r.text)
        if data == "data_box":
            return urlexe,data_box,header
        elif data == "data_shop":
            return urlexe,data_shop,header
    def addCoupon(self,data1):
        data = self.exedata(data1)
        name = ["惊喜专场六折券","惊喜专场七折券","惊喜专场八折券","惊喜专场九折券"]
        value_69 = [2700,2000,1300,600]
        value_59 = [2300,1700,1100,500]
        value_399 = [15900,11900,7900,3900]
        value_899 = [35900,26900,17900,8900]
        for a in range(0,4):
            data[1]["couponTemplate"]["name"] =name[a]
            data[1]["couponTemplate"]["value"] = value_899[a]
            print(data[1])
            r = requests.post(url=data[0],json=data[1],headers=data[2])
            print(r.text)
            time.sleep(1)

if __name__ == '__main__':
    a = AddCouponTemplate()
    a.addCoupon("data_shop")







