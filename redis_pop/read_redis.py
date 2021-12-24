"""
 -*- coding: utf-8 -*-
 @File  : read_redis.py
 @Author: yanjie
 @Date  : 2021/12/8 4:49 下午
 @功能描述  :redis数据的配置读取
 @实现步骤：
    1.导包
    2.连接redis
    3.获取数据
    4、删除key值
"""
# 1.导包
import redis,json
class Rsdis():
    def connection_resid(self):
        # 2.连接redis
        # self.r = redis.Redis(host="10.110.203.201", port=6379, db=1, password="z9SdeWy8aiZgqGX2", encoding="utf-8")
        self.r = redis.Redis(host="r-2zel7jhfxuulhcytl3.redis.rds.aliyuncs.com", port=6379, db=4, password="Rfy2ymvb3%BzfMu#", encoding="utf-8")

        return self.r
    def delete_key(self,keys):
        r = self.connection_resid()
        # 3.获取数据
        # data = r.get("admin_send_coupon_ids")
        #转化为json格式
        # da = json.loads(data)
        # 4、删除key值
        #admin_send_coupon_ids
        result = r.delete(keys)
        return result
if __name__ == "__main__":
    re = Rsdis()
    keys = "activity:voteDiscount:voteDiscount_20211216:day:1:voteId:8438568"
    keys1 = "activity:voteDiscount:voteDiscount_20211216:day:1:discountValue:8438568"
    keys2 = "activity:voteDiscount:voteDiscount_20211214a:day:2:couponNum:6768918"  #是否领取优惠券，不删也行
    print(re.delete_key(keys))
    print(re.delete_key(keys1))
