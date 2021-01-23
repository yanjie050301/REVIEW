# age = 18
# name = "yanjie"
# # 我的名字打印
# print("我的名字是%s"% name)
# print("我的体重是%03d" % age)
# print(F"我的名字是{name},我的年龄是{age},去年我{age-1}岁")
# print("我的%.1f"% age)
# def man():
#     weight = input("你今年多少岁？请输入")
#     print(f"明年你就是{int(weight)+1}")
# man()
# def data_type():  #数据类型
#     age=input("请输入您的年龄：")
#     print("输入的类型为",type(age))
# data_type()
# def fuzhi():
#     a=b=input("请输入：")   #同时赋值
#     print(a,b)
#     d,f,g=1,2,3           #多个变量赋值
#     print(f)
# fuzhi()
# def bijiao():    #逻辑运算符
#     a = 1
#     b = 2
#     c = 3
#     e = (a>b)and(b>c)
#     f = (a>b)or(b>c)
#     r = not(a>b)
#     print(e,f,r)
# bijiao()
# def string():   #字符型切片
#     a = "shdfskfhsfhjk"
#     b = a[2:4:1]
#     e = a[9:2:-1]
#     print(b)
#     print(e)
# string()
# def find_lianxi():   #查找函数
#     mystr = "hello world and supertest and chaoge and Python"
#     mystr = "hello world and supertest and chaoge and Python"
#     print(mystr.find("and"))   #查找and字符，从左往右数，找第一个and
#     print(mystr.find("and",2,10))  #查找and字符，从左往右数，范围从第2到第10个字符，找第一个and
#     print(mystr.rfind("and")) #查找and字符，从右往左数，找第一个and
#     print(mystr.find("b"))    #查找b字符，从左往右数，找第一个b,没有显示-1
#     print(mystr.index("and"))   #查找and字符，从左往右数，找第一个and
#     print(mystr.index("b"))     #查找b字符，从左往右数，找第一个b,没有会报错
# find_lianxi()
# def repleace():    #替换函数
#     mystr = "hello world and supertest and chaoge and Python"
#     print(mystr.replace("and","1"))  #将and全部替换为1
#     print(mystr.replace("and","ddd",2))  #将and替换为ddd,从左往右只替换2个and
# repleace()
# def split():   #分割函数
#     mystr = "hello world and supertest and chaoge and Python"
#     print(mystr.split("and"))   #以and为分隔字符，分割mystr字符串，同时and消失
#     print(mystr.split("and",2))   #以and为分隔字符，分割mystr字符串，分割2次，同时and消失
#     print(mystr.split(" "))      #以空格为分隔字符，分割mystr字符串，同时空格消失
# split()
# def join():   #用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
#     mystr = "hello world and supertest and chaoge and Python"
#     a = ["a","b","d"]
#     b = ("a","b","d")
#     print("_".join(mystr)) #将mystr字符串每个字符都用下划线连接
#     print("ddd".join(a))    #将列表a每个字符都用ddd连接
# join()
# def daxiaoxie():   #字符串大小写练习函数
#     mystr = "Hello world And supertest and chaoge and Python"
#     print(mystr.capitalize())   #将字符串mystr的第一个字符转换为大写，若后面是大写，则转换为小写
#     print(mystr.title())    #将字符串mystr的每个单词的首字母转换为大写
#     print(mystr.lower())    #将字符串mystr中的大写转换为小写
#     print(mystr.upper())    #将字符串mystr中的小写转换为大写
# daxiaoxie()

# def delete_str():        #删除字符串左右的空格符
#     mystr ="    kuaixiakele   "
#     print(mystr.lstrip())   #删除字符串左边的空格符
# delete_str()
# def if_lianxi():    #if练习
#     a = int(input("请输入一个数字："))
#     if a > 0 :
#         print("您输入的数字大于0")
#     else:
#         print("您输入的数字小于0")
# if_lianxi()
# def elif_lianxi():   #elif练习
#     age = int(input("请输入您的年龄："))
#     if age>=0 and age<18:
#         print("您是童工")
#     elif age>=18 and age<60:
#         print("合法搬砖")
#     elif age>60:
#         print("您退休了")
#     else:
#         print("您输入的不正确")
# elif_lianxi()
# def if_if():    #if嵌套练习
#     money = int(input("请输入卡内余额："))
#     if money>0:
#         zuowei = int(input("请输入空座位数："))
#         if zuowei>0:
#             print("坐着去吧")
#         else:
#             print("站着去吧")
#     else:
#         print("穷光蛋")
# if_if()
# def while_lianxi():   #while练习
#     n = 0
#     while n<10:
#         print("下课吧")
#         n = n+1
# while_lianxi()
# def Continue():    #Ccontinue练习
#     n = 1
#     while n<6:
#         if n ==3:
#             print("我饱了，不想吃了")
#             n=n+1
#             continue            #停止当前循环，进行下一轮循环
#         print(f"我吃了第{n}个苹果")
#         n = n + 1
# Continue()
# def Break():    #break练习
#     n = 1
#     while n <6:
#         if n == 4:
#             print(f"我不吃了")
#             break            #停止所以循环
#         print(f"我吃了{n}个苹果")
#         n = n+1
# Break()
