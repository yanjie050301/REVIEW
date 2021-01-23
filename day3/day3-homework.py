import random
# 有三个办公室，8位老师，8位老师随机分配到3个办公室
"""
teacher = ["赵","钱","孙","李","周","吴","郑","王"]
offices =[[],[],[]]
for name in teacher:
    num = random.randint(0,2)     #随机取办公室下标
    offices[num].append(name)      #将遍历的老师放在办公室中
i = 1
for office in offices:
    print(f"办公室{i}的人数是{len(office)}")
    i = i+1
    for name in office:
        print(name,end="   ")
    print("-"*5)
"""

# 将list列表中小强全部删除（作业）
"""
list1 = ["小红","小强","小明","小强","小孙","小强","小眼"]
list2 = ["小强"]
list3 = []
for n in list1:              #遍历list1中的名字
    if n not in list2:      #判断名字是否与小强一致，不一致的放入新的列表中
        list3.append(n)
print(list3)
"""
# 打印多条横线
"""
 def heng():
    print("-"*15)
a = int(input("请输入打印的行数"))
for a in range(1,a+1):
    heng()
"""
#求三个数之和
"""
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
c = int(input("请输入第三个数："))
def sum(w,e,r):
    return w+e+r
sum1 = sum(a,b,c)
print(f'{a}+{b}+{c}={sum1}')
"""
    
#1.使用列表推导式生成能被5整除的数（100以内）
# list1 = [i for i in range(1,100) if i%5==0]
# print(list1)
# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
"""
name = ["小红","小强","小明","小强","小孙","小强","小眼"]
age = [11,12,13,14,15,16,17]
dict = {}
a = 0
while a<len(name):
    dict[name[a]] = age[a]
    a = a+1
print(dict)
"""
# 3.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},xxx]
# ----------------
# *   1-新增用户
# *   2-查询用户
# *   3-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息
"""
dict = {"yj": 33,"jj": 33,'uu': 33}
def page():
    print("1-新增用户")
    print("2-查询用户")
    print("3-删除用户")
    print("4-退出系统")
    global num
    num = int(input("请输入功能编号："))
def add_student(name,age):     #新增用户
    if name in dict.keys():          #判断新增用户是否已存在
        print("该用户已存在")
    else:
        dict[name] = age
        print("目前用户列表为：",dict)
        return 0

def select_student(name):        #查询用户
    if name in dict.keys():
        for name1 in dict.keys():   #遍历字典查询用户
            if name1 == name:
                age1 = dict.get(name1)
                print('您查询的信息为：姓名：',name,'，年龄：',age1)
    else:
        print("查询的用户不存在！")

def del_student(name):      #删除用户
    if name in dict.keys():
        del dict[name]
        name1 = dict.get(name)
        if name1 not in dict.keys():      #判断是否真正删除
            print(name,"用户已删除！！！")
    else:
        print("删除的用户不存在！")
def exit():
    print("已退出系统")
def system():
    page()
    if num == 1:
        name = input("请输入新增用户姓名：")
        age = int(input("请输入用户年龄："))
        add_student(name,age)
    elif num ==2:
        name = input("请输入查询用户姓名：")
        select_student(name)
    elif num == 3:
        name = input("请输入要删除的用户姓名：")
        del_student(name)
    elif num ==4:
        exit()
    else:
        print("输入错误，请输入正确的编号！！")
system()
"""

# 作业：读取data文件中的数据，将所有的数字按照从小到大的顺序写入backup文件
f = open("data.txt","+r")
line = f.readlines()
# print(line[5])
list1 = []
for a in line:
    list1.append(a)
print(list1)
print(min(list1))
# Python练习题：
# 1、打印小猫爱吃鱼，小猫要喝水
# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
#
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量