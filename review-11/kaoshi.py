#1. 有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转
"""
str = "welocme to super&Test"
str1 = []
a =len(str)-1
while a>=0:     #将字符串倒叙添加到列表中
    str1.append(str[a])
    a = a-1
print(str1)
c = ""
for b in str1:    #遍历列表
    c = c+b        #拼接成字符串
print(c)
d = c.split(" ")  #以 分割字符串，并命名为d列表
e = len(d)-1
while e>=0:      #倒叙获取列表，并以字符串的形式打印
    print(d[e],end=" ")
    e = e-1
"""
# 2.当前文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
# lucy:21，tom:30
# xiaoming:18，xiaohong:15
# xiaowang:20，xiaohei:19
# 请输出年龄大于18岁的人名

"""
#打开data.txt文件
f = open("data.txt","+r",encoding = "utf-8")
# 将内容resdline一行一行读出来,读取第一行
#定义一个新字典
dict ={}
a = 1
while a<100:
    a = a + 1
    line = f.readline()
    if line =="" :
        break
    print(f"*******第{a-1}遍循环读取出第{a-1}行数据为：{line}")
# 使用split拆分开
    line1= line.split("，")
    print(f"第一次以逗号拆分：{line1}")
    for b in range(0,len(line1)):
        line2 = line1[b].split(":")
        print(f"第二次以冒号拆分：{line2}")
        # 将拆分好的人名和年龄组成键值对添加到字典中,组成字典
        dict[line2[0]] = line2[1]
        print(f"此时的字典值为{dict}")
#将字典的键keys放在一个列表
keys = []
for key in dict.keys():
    keys.append(key)
print(f"keys的列表为{keys}")
#将字典的值values放在一个列表
values = []
for value in dict.values():
    values.append(value)
print(f"values的列表为{values}")
# 将字典values遍历
for c in values:
#  判断是否大于18岁
    t = int(c)        #将字符串转化为数字
    if t > 18:
        d = values.index(c)    #通过索引获取数据在列表中的下标
#通过下标找到keys的值
        f = keys[d]
        print(f"大于18岁的人名有{f}")
#关闭文件
f.close()
"""
# 3.递归实现斐波那契数列
#正常写法
# list1 = [0,1]
# b =0
# while b<5:
#     b= b+1
#     c = list1[b]+list1[b-1]
#     list1.append(c)
# print(list1)
#递归函数写法
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
list1 = []
for x in range(10):
    a = fibonacci(x)
    list1.append(a)
print(list1)
"""
# 4.debug的快捷键：f8/f7/f9分别的作用
"""
f7:遇到方法体进入方法体内部，挨个方法执行
f8：一步一步执行
f9：按照断点，一个断点一个断点执行
"""