"""
需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：生的
3-5分钟：半生不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
用户可以按自己的意愿添加调料
"""
"""
# 定义一个地瓜类，参数有时间,初始值为0
class Sweet():
    def __init__(self):
        self.time = 0
    def cook(self,time):
        self.time = self.time + time
        # 判断烤地瓜的时间，根据不用的时间输出地瓜不同的状态
        if 0<self.time <=3:
            self.static = "生的"
        elif 3<self.time<=5:
            self.static = "半生不熟"
        elif 5<self.time<=8:
            self.static = "熟的"
        elif self.time>8:
            self.static = "糊了"
    def __str__(self):
        return f"该地瓜烤了{self.time}分钟，目前状态为{self.static}"
# 定义一个调料类，参数为调料
class Tiao():
    def tiaoli(self,tiaolia):
        self.tiaolia = tiaolia
    def __str__(self):
        # 根据用户给的调料输出地瓜的口味
        return f"目前该地瓜是{self.tiaolia}味"
digua = Sweet()
digua.cook(5)
print(digua)
tiaolioa = Tiao()
tiaolioa.tiaoli("la")
print(tiaolioa)
"""
