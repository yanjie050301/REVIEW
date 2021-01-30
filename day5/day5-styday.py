#多态联系



#创建一个方法
# import my_module1
# my_module1.testA(1,3)
#如果使⽤ from .. import .. 或 from .. import * 导⼊多个模块的时候，且模块内有同名功能。当调
# ⽤这个同名功能的时候，调⽤到的是后⾯导⼊的模块的功能。
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












#####异常的传递



