list = ["小红","小强","小明","小强","小孙","小强","小眼"]
list1 = ["dsd","fasf","asfasf"]
name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
#查找小红是否在list列表中，结合范围
# print(list.index("小明",0,1))
#统计小强在列表中出现的次数
# print(list.count("小强"))
#统计列表的长度
# print(len(list))
#在列表中增加小郭
# list.append("小郭")
# print(list)
#在列表中增加闫洁和肖杰
# l = ["yanjie","xiaojei"]
# d = list+l
# print(d)
#在列表中删除小眼
# list.remove("小眼")
# print(list)
#拼接list和list1，并且打印出来
# print(list+list1)
#将海明添加到list列表第5个位置
# list.insert(4,"haiming")
# print(list)
#删除list1列表
# del list1
# print(list1)
#删除list最后一个数据
# list.pop()
# print(list)
#删除list列表第3个数据，并打印删除数据
# a = list.pop(2)
# print(a)
#将list列表中小强全部删除（作业）
# for a in list:
#     if a =="小强":
#         list.remove(a)
# print(list)
#将list中小红改为小绿
# list[0]="小绿"
# print(list)
# for a in range(0,len(list)-1):
#     if list[a] == "小红":
#         list[a] ="xiaolv"
# print(list)
#将list表中数据倒叙并打印
# list.reverse()
# print(list)
#将list表中的数据排序，按照默认排序
# list.sort()
# print(list)
#将list表中复制，重命名为list123，并打印
# list123= list.copy()
# print(list123)
#将list中的小红打印
# for a in list:
#     if a == "小红":
#         print(a)
tup = (1,2,3,4,[5,8,9,6])
#定义一个元组，里面只有一个数据，并打印
# t = ("ww00",)
# print(type(t))
#打印tup元组里边的3
# print(tup[2])
#查找数据2是否在tup元组中
# print(tup.index(2))
#将tup元组中8改为99
# tup[4][1] = 99
# print(tup)

dict = {"a":"12",'b': 23,"c":"sdsd","d":888}
#将f=12键值对新增到dict字典中
# dict["f"] = "2"

#将键值对a的值改为qwer
# dict["a"] = "qwer"

#删除字典dict
# del dict
#删除字典值d=888的键值对
# del dict["d"]
#清空字典并打印
# dict.clear()
#查找key为a的键值对是否在字典dict中并打印
# if "a" in dict.keys():
#     print(f'a:{dict["a"]}')
#查找key为t的键值对是否在字典dict中，若没有默认返回000并打印
if "t" not in dict.keys():
    print(000)
#取字典中所有的key并打印
#取字典中所有的values并打印
#取字典中所有的键值对并打印
#遍历字典中所有的key并打印
#遍历字典中所有的values并打印
# 遍历字典中所有的元素并打印
#遍历字典中所有的键值对并打印
print(dict)


s1 = {10,20,30,"ddd",40,50,60}
#将56添加到集合s1中并打印
#将[44,"ssd",0000]添加到集合s1中
#删除集合s1
#删除集合s1中的ddd数据
#删除集合s1中ccc数据
#随机删除集合s1中的数据，并打印删除数据
#判断565是否在集合中



