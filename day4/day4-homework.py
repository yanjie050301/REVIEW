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
"""
# 定义一个房子类，一个放家具的方法，
class Home():
    def __init__(self,area,huxing):
        #房屋剩余面积
        self.area = area
        # 房屋总面积
        self.zong = area
        #家具列表
        self.jiaju_list = []
        #房屋户型
        self.huxing = huxing

    # def __str__(self):
    #     return f"房子户型为{self.huxing}，总面积为{self.zong}，添加了{self.jiaju}家具，剩余面积为{self.area}，家具列表为{self.jiaju_list}"

    def add_jiaju(self,jiaju,jiaju_area):
        self.jiaju = jiaju
        #判断家具的面积是否比房屋面积大
        if jiaju_area>self.area:
            print("家具过大")
        else:
            #剩余=房屋面积-家具面积
            self.area = self.area-jiaju_area
            #将家具添加到家具列表中
            self.jiaju_list.append(jiaju)
            print(f"房子户型为{self.huxing}，总面积为{self.zong}，添加了{self.jiaju}家具，剩余面积为{self.area}，家具列表为{self.jiaju_list}")

home = Home(200,"别墅")
home.add_jiaju("床",4)
home.add_jiaju("衣柜",2)
home.add_jiaju("餐桌",1.5)
"""
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

# 定义一个士兵类，有开火和装子弹的方法
"""
class Shibing():
    def __init__(self,ren_name,qiang_name):
        #士兵的名字
        self.ren_name = ren_name
        #枪的名字
        self.qiang_name = qiang_name
        #枪的子弹
        self.zongzidan = 5
        #枪剩余子弹
        self.shengzidan = 5
    def kaihuo(self):
        #士兵开一枪，子弹-1
        self.shengzidan = self.shengzidan - 1
        print(f"{self.ren_name}拿着{self.qiang_name}，当前子弹数量为{self.zongzidan}，开了一枪，子弹剩余{self.shengzidan}")
    def zhuagzidan(self):
        print(f"{self.ren_name}拿着{self.qiang_name}，当前子弹数量为{self.shengzidan}，",end="")
        # 士兵装子弹，子弹+1
        self.shengzidan = self.shengzidan + 1
        print(f"装一下子弹，子弹剩余{self.shengzidan}")
ruien = Shibing("ruien","AK47")
ruien.kaihuo()
ruien.zhuagzidan()
"""
class Qiang():
    def __init__(self,qiang_name,num):
        # 枪的名字
        self.qiang_name = qiang_name
        # 枪的子弹
        self.zongzidan = num
        # 枪剩余子弹
        self.shengzidan = num
class Shibing(Qiang):
    def __init__(self,ren_name,qiang_name,num):
        #士兵的名字
        self.ren_name = ren_name
        self.qiang_name = qiang_name
        self.shengzidan = num
        self.zongzidan = num
    def kaihuo(self):
        #士兵开一枪，子弹-1
        self.shengzidan = self.shengzidan - 1
        print(f"{self.ren_name}拿着{self.qiang_name}，当前子弹数量为{self.zongzidan}，开了一枪，子弹剩余{self.shengzidan}")
    def zhuagzidan(self):
        print(f"{self.ren_name}拿着{self.qiang_name}，当前子弹数量为{self.shengzidan}，",end="")
        # 士兵装子弹，子弹+1
        self.shengzidan = self.shengzidan + 1
        print(f"装一下子弹，子弹剩余{self.shengzidan}")
ruien = Shibing(ren_name="ruien",qiang_name="AK47",num=10)
ruien.kaihuo()
ruien.zhuagzidan()

# 有这样一个文件，文件内容如下：
# Lucy|18601914231|男|19890218
# Jack|18101913132|女|19810311
# Tom|18201912533|女|19830713
# Lily|18301911734|男|19870210
# 任务1-找出所有L开头的人名
# 任务2-按照年龄进行排序
# 任务3-找出所有女性用户的信息
import os
"""
# 1.创建一个新的文件data.txt
file = "data.txt"
# 获取当前路径
path =os.getcwd()
print(path)
# 拼接新路径
new_path = path + "//" + file
f = open(new_path,"w",encoding="utf-8")
lis = ["Lucy|18601914231|男|19890218","Jack|18101913132|女|19810311","Tom|18201912533|女|19830713","Lily|18301911734|男|19870210"]
# 2.将内容一次写入文件中
for a in lis:
    f.write(a)
    f.write("\n")
f.close()
"""
######### 任务1-找出所有L开头的人名
"""
new_f= open("data.txt","+r",encoding="utf-8")
list1 = []
while True:
    a = new_f.readline()     #将文件依次读出来，放入列表中
    if len(a) == 0:
        break
    list1.append(a)
# print(list1)
for b in list1:          #遍历列表
    if b.startswith("L"):    #判断元素是否以F开头，是的话，打印
        print(b)
f.close()
"""
######### 任务2-按照年龄进行排序
"""
new_f= open("data.txt","+r",encoding="utf-8")
list_age = []
list_person = []
while True:
    a = new_f.readline()     #将文件依次读出来，放入列表中
    if len(a) == 0:
        break
    list_person.append(a)
    b = a.split("|")[3]      #分割字符串并获取出生日期# 提取出出生年月，组成一个新的列表
    b = b.rstrip()           #删除出生日期右边的空字符
    list_age.append(b)       #将获取的日期添加到列表中
list_age.sort()              #将列表中日前从小到大排序
# print(list_age)
# print(list_person)
#拿日期去遍历用户信息，如果包含该日期，则打印
for m in list_age:
    for n in list_person:
        if m in n:
            print(n)
new_f.close()
"""
######### 任务3-找出所有女性用户的信息
"""
new_f= open("data.txt","+r",encoding="utf-8")
list_person = []
while True:
    a = new_f.readline()     #将文件依次读出来，放入列表中
    if len(a) == 0:
        break
    list_person.append(a)
for person in list_person:
    if "女" in person:
        print(person)
new_f.close()
"""
# 练习：
# 目录下有这些文件：
# A1.txt
# B2.txt
# C1.doc
# D1.excel
# 任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等
"""
import os,shutil
"""
# os.mkdir("file")
path = os.getcwd()
new_path = path + "\\"+"file"+"\\"
with open(new_path + "A1.txt",mode="a") as fp:
    fp.write("\n")
with open(new_path + "B2.txt",mode="a") as fp:
    fp.write("\n")
with open(new_path + "C1.doc",mode="a") as fp:
    fp.write("\n")
with open(new_path + "D1.excel",mode="a") as fp:
    fp.write("\n")
"""
# 拿到当前目录下所有的文件， os.listdir(path)
path = os.getcwd()
new_path = path + "\\"+"file"
file = os.listdir(new_path)
# 获取文件的后缀，分割   os.path.splitext(path)
dir_tupe = set() #新建一个元祖，去重
a = 0
while a<len(file):
    path1 = new_path + "\\"+file[a]   #组成完整的文件路径
    f1,f2 = os.path.splitext(path1)      #分割路劲与后缀名
    dir = f2.lstrip(".")               #去除左边的“.”
    dir_tupe.add(dir)  #往元祖中添加元素
    a = a+1
# print(dir_list)
for b in dir_tupe:
    os.mkdir(new_path+"\\"+b)    #创建新的文件夹
    for c in file:
        if b in c:     #判断文件的后缀是否与文件夹名字一致
            shutil.move(new_path + "\\" +c,new_path+"\\"+b)        #一致的话，将文件移动到该文件夹下面
# 移动文件进入不同的文件  shutil.move()

"""








