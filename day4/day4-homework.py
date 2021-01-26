# 1、打印小猫爱吃鱼，小猫要喝水
"""
# 定义一个动作类，有吃鱼和喝水两个方法
class Action():
    def __init__(self,dongwu):
        self.dongwu = dongwu
    def eat(self):
        print(f"{self.dongwu}要吃鱼")
    def druik(self):
        print(f"{self.dongwu}要喝水")
dw = Action("小猫")
dw.eat()
dw.druik()
"""

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤


"""
# 定义一个人名类，有跑步方法和吃东西方法
class Man():
    def __init__(self,name,weight):
        self.weight = weight
        self.name = name
    #定义一个姓名方法
    def namea(self):
        print(f"{self.name}之前的体重为{self.weight}kg")
    #定义一个跑步方法
    def run(self):
        print(f"{self.name}之前的体重为{self.weight}kg，",end="")
        self.weight = self.weight - 0.5
        print(f"跑了一次步后，体重为{self.weight}kg")
    # 定义一个吃东西方法
    def eat(self):
        print(f"{self.name}之前的体重为{self.weight}kg，", end="")
        self.weight = self.weight + 1
        print(f"吃了一顿饭后，体重为{self.weight}kg")
xiaom = Man("小明",75.0)
xiaom.run()
xiaom.eat()
xiaomei = Man("小美",45)
xiaomei.namea()
"""


# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表









# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
