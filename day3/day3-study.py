# def select_func():
#     print("------请选择功能-------")
#     print("查询余额")
#     print("存款")
#     print("取款")
#     print("========请选择功能=======")
# print("密码正确登录成功")
# select_func()
# print("查询余额完毕")
# select_func()
# print("取了200元")
# select_func()

# def sum(a,b):
#     """计算两数之和"""
#     return a+b
# m = sum(4,6)
# print(m)


#嵌套函数练习
# def testB():
#     print("======startB=====")
#     testA()
#     print("======endB====")
# def testA():
#     print("-----startA------")
#     print("-----执行代码------")
#     print("------endB------")
# testB()

#局部变量    只能在函数内部使用
# def fun1():
#     a =100
#     print(a)
# fun1()
# # print(a)    #会报错
# #全局变量         全局都可以使用
# b = 202
# def fin2():
#     print(b)
# def fin3():
#     print(b+6)
# fin2()
# fin3()

#定义一个全局变量
# glo_num = 0
# def test1():
#     #修改全局变量
#     global glo_num
#     glo_num = 100
# def test2():
#     print(glo_num)
# test1()
# test2()
#返回值作为参数传递
# def fun1():
#     return 50
# def fun2(a):
#     print(a)
# b = fun1()
# fun2(b)
#一个函数只能有一个return,若多个return，只返回第一个return
# def fun1():
#     return 20
#     return 30
# a = fun1()
# print(a)
#若想返回多个值，则用逗号隔开
# def fun1():
#     return 1,2,3
# a = fun1()
# print(list(a))     #返回的类型默认是元组，也可以转换为其他类型

#位置参数练习
# def user_info(name,age,sex):
#     print(f'姓名是{name}，年龄是{age}，性别是{sex}')
# user_info("yanjie",12,"nv")    #参数值和参数的位置要一一对应
# user_info(12,"nv","yanjie")     #不一一对应的情况
# user_info("yanjie",sex="nv",age=12)    #也可以使用键值对的情况进行给值【位置参数必须在关键字参数的前面】
# user_info(sex="nv",age=12,"yanjie")     #关键字函数在前面，会报错

#缺省参数练习
# def fun1(name,sex,age = 18):            #缺省参数缺省值只能放最后，不能放中间
#     print(f'姓名是{name}，年龄是{age}，性别是{sex}')
# fun1("yanjie","nv")      #age不给传参数，就是用默认参数
# fun1("yanjie","nv",55)   #age传参数，则使用给的参数
#不定长参数练习---包裹位置传递     #用于不确定有几个参数
# def fun1(*args):
#     print(args)
# fun1("yanjie",45,"111")
# li = [4,2,3]
# fun1(li)            #把列表当成整元素传给函数
# fun1(*li)           #取列表每个值传给函数  要加*

#不定长参数练习---包裹关键字传递
# def fun1(**kwargs):
#     print(kwargs)
# fun1(name = "yanjie",age = 18,sex = "nv")        #键值对形式的字典
# dict1 = {'name': 'yanjie', 'age': 18, 'sex': 'nv'}
# fun1(**dict1)              #取字典每个键值对传给函数，要加**
# # fun1(dict1)              #不加**，会报错

def fun(**kwargs):
    print(kwargs)

# fun(a = "1",b = "2")
# di ={'a': '1', 'b': '2'}
# fun(**di)



#可变类型和不可变类型
# def test1(a):
#     print(a)
#     print(id(a))
#     a += a
#     print(a)
#     print(id(a))
# b = 100
# test1(b)
# c = [11,22]
# test1(c)

#递归函数,自己调用自己
# def sum(num):
#     if num ==1:
#         #如果是1，直接返回1
#         return 1
#     return num + sum(num-1)
# a = sum(5)
# print(a)
#高阶函数
# def fun1(a,b):
#     return abs(a) + abs(b)
# print(fun1(3,13))
# #转换为高阶函数
# def fun2(a,b,f):
#     return f(a)+f(b)
# a = fun2(2,-5,abs)
# b = fun2(2.3,5.6,round)
# print(a,b)
# 【【【【【【】】】】】】
import functools
# list1 = [1,2,3,4,5]




#文件的操作
# # 1.打开⽂件
# f = open("test.txt","r+",encoding="utf-8")
# # 2. 读写等操作
# # f.write("1111111")
# #按照⾏的⽅式把整个⽂件读取,以列表的形式，每行为一个元素进行显示
# # a = f.readlines()
# # print(a)
# #一次读取一行内容
# b = f.readline()
# print(b)
# #查看光标的位置
# c = f.tell()
# print(c)
# #移动光标的位置
# f.seek(0)        #将光标移动到文件开头
# f.seek(3)        #将光标移动到第三个字节后面，文件以字节为单位，数字占一个字节，汉字占3个字节
# f.seek(0,0)      #将光标移动到文件开头
# f.seek(0,1)      #将光标移动到文件当前位置
# f.seek(0,2)      #将光标移动到文件结尾
# f.write("2222")
# d = f.tell()
# print(d)
# # 3. 关闭⽂件
# f.close()

#文件备份




#os操作  文件和文件夹的操作
import os
#重命名文件
# os.rename("data.txt","data1.txt")
#删除文件
# os.remove('data.text')
#创建文件夹
# os.mkdir("text")
#删除空文件夹，若文件夹不为空，则报错
# os.rmdir("text")
#查看文件当前位置
# a = os.getcwd()
# print(a)
#改变默认位置
# os.chdir("F:\\test\\selenium\\untitled\\REVIEW\\day2")
# b = os.getcwd()
# print(b)
#查看路径下的所有文件
# list1 = os.listdir()
# print(list1)
path = os.path.dirname(__file__)
print(path)
