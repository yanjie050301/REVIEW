#一、列表
# list = ["abc","def","ghi","jkl","abc","abc"]
# print(list[0])    #用下标进行控制输出
# print(list.index("jkl",1,4))     #查找某个变量值，遵循顾前不顾后
# print(list.count("abc"))           #统计数据出现的次数
# print(len(list))                #统计列表长度，既列表中数据的个数

# name = ["小红","小强","小明","小孙","小眼"]
# name1 = input("请输入一个值：")
# if name1 in name :
#     print("该值在name列表中")
# else:
#     print("该值不在name列表中")
# print(name.index(12))
# name.append("xiaoguo") #加入列表一个数据
# name.extend(["dksjh","sldkj"])  #加入列表多个数据
# name2 = ["ed","seff","fsfsf"]
# name = name + name2               #拼接字符串
# name.insert(0,"sdkh")        #指定位置添加数据
# del name[2]             #根据下标删除某个数据
# print(name)
# name.pop()             #默认删除最后一个数据
# w = name.pop(0)            #删除指定数据，并且返回该值
# name[0] = "aaaaa"        #x修改列表中的数据
# name.reverse()            #将列表中数据倒叙
# print(name)
# name.sort()                #将列表排序默认按照ASCII码表排序
# name1 = name.copy()           #复制某个列表
# print(name1)
# name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
# name = name_list[2][0]              #取值
# print(name)

#二、元组，定义之后不可以改变
# tup1 = (1,2,3,4)
# print(type(tup1))
# # tup2 = (5,)                            #tupe里面如果只有一个数据，后面要加逗号,不加逗号数据类型是str,加逗号数据类型才是元组
# # print(type(tup2))
# num = tup1[2]
# print(num)                     #元组取值
# print(tup1.index(3))            #查找数据
# tup2 = (1,2,3,4,[5,8,9,6])
# tup2[4][0]=66                        #修改元组里边列表的数据
# print(tup2)


#三、字典      没有顺序，无法用下标引用
c = {"a":"12"}
c["b"] = 23          #新增一个键值对
# c["a"] = 22          #修改a的值
# del c["a"]            #删除键值对
# del c                  #删除字典
c["d"] = 3
c["e"] = 55
# num = c["d"]              #取值，若没有则报错
# num1 = c.get("f",22)        #取值，没有返回None，或者返回给的默认值
# list = c.keys()                #取值，取字典中所有的key
# values = c.values()          #取值，取字典中所有的值
# dict1 = c.items()              #取值，以键值对的形式取值
# for key in c.keys():          #遍历字典中所有的key
#     print(key)
# for values in c.values():        #遍历字典中所有的值
#     print(values)
# for item in c.items():        #遍历字典中所有的键值对
#     print(item)
# for k,v in c.items():
#     print(k,"=",v)



#四、集合
# s1 = {10,20,30,"ddd",40,50,60}      #无序的，不可重复的
# s1.add(100)                  #新增数据
# s1.update([10,20,99])         #新增数据，只能加序列
# s1.remove(10)                 #删除数据，没有则报错
# s1.discard(11)                #删除数据，没有不报错
# b = s1.pop()                        #随机删除集合中某个数，并返回该数据
# a = 10 in s1                  #判断元素是否在集合内
# print(s1,a,b)

# a = range(10)
# a = list(range(10))
# print(a)
# for b in range(1,9,2):
#     print(b)
# a = range(0,10,5)
# for b in a:
#     print(b)

#列表推导式
# list = []
# i =0
# while i<10:
#     list.append(i)
#     i = i+1
# print(list)

# list = []
# for i in range(10):
#     list.append(i)
# print(list)

# list = [i for i in range(10) if i%2==1]
# print(list)

#字典推导式
# list = ["A","B","C"]
# list1 = ["a","b","c"]
# dict = {}
# for i in range(len(list)):
#      dict[list[i]] = list1[i]
# print(dict)
#
#
# dict = {list[i]:list1[i] for i in range(len(list))}
# print(dict)


#集合推导式
jihr = set()
list = [4,5,6]
for i in list:
    a = i**2
    jihr.add(a)
print(jihr)

jihe = {i**2 for i in list}
print(jihe)