# encoding = "utf-8"
############### 多态联系（⼀个抽象类有多个⼦类，因⽽多态的概念依赖于继承）。
# 定义:多态是一种使用对象的方式,方类重写父类方法,调用不同子类对象的相同父类方法，可以
# 产生不同的执行结果
# 好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变
# 化！
# 实现步骤：
# 定义父类，并提供公共方法
# 定义子类，并重写父类方法
# 传递子类对象给调用者，可以看到不同子类执行效果不同
#定义一个父类,拥有公共方法
class Man(object):
    def work(self):
        print("我要干活")
#子类继承父类
class Mini(Man):
    #重写父类同名的方法
    def work(self):
        print("干上班的活")
class Yanjie(Man):
    #重写父类同名的方法
    def work(self):
        print("干下地的活")
# 定义一个新的类，传给不同的对象，打印不同的结果（实现多态）
class Person():
    def work_with_person(self,man):
        man.work()
a = Mini()
c = Yanjie()
b = Person()
b.work_with_person(a)
b.work_with_person(c)


######关于包的导入
#创建一个方法
# import my_module1
# my_module1.testA(1,3)
#如果使用 from .. import .. 或 from .. import * 导入多个模块的时候，且模块内有同名功能。当调用
# ⽤这个同名功能的时候，调用到的是后面导入的模块的功能。
# from my_module1 import testA
# from my_module2 import testA
# testA(1,2)   #只调用了my_module2的方法


#####异常#######
# try:
#     open("text.txt","r")
# except:
#     open("text.txt","w")


##指定异常
# try:
#     print(num)
# #如果不是这个类型的错误，则无法捕获异常
# except NameError:
#     print("num有错误")



###捕获多个指定异常
# try:
#     print(1/0)
# except (ZeroDivisionError,NameError):
#     print("0不能做除数")


####捕获异常描述信息
# try:
#     print(1/0)
# except (ZeroDivisionError,NameError) as massage:
#     print(massage)



####捕获所以异常
# try:
#     print(1/0)
# except Exception as massage:
#     print(massage)


####异常中的else  没有异常则执行else

# try:
#     print(1)
# except Exception as msg:
#     print(msg)
# else:
#     print("我是else，是没有异常的时候执行的代码")




####异常中的finally   不管有无异常，都会执行
# global f
# try:
#     f = open("text.txt","r")
# except Exception as msg:
#     print(msg)
# else:
#     print("没有异常")
# finally:
#     print("finally执行")
#     f.close()




#####异常的传递
"""
import time
try:
    f = open("text.txt")
    try:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            time.sleep(2)
            print(line)
    except:
        print("意外终止了读取数据")
    finally:
        f.close()
        print("关闭文件")
except:
    print("没有这个文件")
"""


#####自定义异常  raise
# 需求：密码长度不足，则报异常（用户输入密码，如果输入的度不足3位，则报错，即抛出自定义异常，并捕获该异常）
"""
#1.自定义异常类，继承Exception
class Aoto_except(Exception):
    #传入用户输入密码的长度和最小长度
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len

    # 定义一个异常输出信息
    # __str__()方法，打印对象的描述，不用调用，自行打印
    def __str__(self):
        return f"您输入的密码长度为{self.length},密码长度必须大于{self.min_len}"
def input_msg():
    try:
        # 用户输入密码
        msg = input("请输入密码：")
        # 判断输入的密码是否符合长度，不符合长度调用自定义异常
        if len(msg)<=3:
            raise Aoto_except(len(msg),3)
    except Exception as massage:
        print(massage)
    else:
        print("密码输入完成")
input_msg()
"""
