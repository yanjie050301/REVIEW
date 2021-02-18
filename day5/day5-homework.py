# 1-课上的所有代码重新敲一遍
# 2-http协议的组成，状态码含义；

# http协议组成：请求头、请求体、请求方式，状态头，状态码，状态体
# 200：接口请求成功
# 3xx:重定向
# 4xx:客户端错误
# 5xx:服务器错误

# 3-完成手机app抓包

# 4-get和post区别

# get：参数跟在地址后面，有长度限制，最长225，无请求体，安全性没有post高
# post：参数单独放在请求体中，无长度显示，安全性高

# 5-cookie和session区别

# cookie是存放在客户端确认用户信息
# session是存放在服务器端确认用户信息

# 6-预习request文档
# 7.复习多态
# 介绍：有一个公共的父类，子类继承父类，重写父类同名的方法，调用不同子类的相同方法，可以产生不同的效果
"""
class Work():
    def work_tpye(self):
        print("谁在工作")
class Xiaoming(Work):
    def work_tpye(self):
        print("小明在工作")
class Xiaohua(Work):
    def work_tpye(self):
        print("小花在工作")
class Who_work(Work):
    def work_shui(self,who):
        who.work_tpye()
a = Xiaoming()
b = Xiaohua()
c = Who_work()
c.work_shui(b)
c.work_shui(a)
"""

#8.捕获异常except、else、finally的区别

# except:发生异常时执行的代码
# else：没有出现异常时执行的代码
# finally：不管有无异常，都要执行
# 顺序必须是except、else、finally
"""
try:
    a = int(input("请输入数字"))
    if a<3:
        print(f"{a}小于3")
except Exception as msg:
    print(msg)
else:
    print("没有异常")
finally:
    print("执行完毕")
"""

#####异常的传递
# 需求：
# 1. 尝试只读方式打开test.txt文件，如果文件存在则读取⽂文件内容，文件不存在则提示⽤用户即可。
# 2. 读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序，则 except 捕获异常,并提示用户。
"""
import time
try:
    f = open("text.txt","r")
    try:
        while True:
            line = f.readline()
            time.sleep(2)
            if len(line) == 0:
                break
            print(line)
    except:
        print("用户意外终止")
    finally:
        f.close()
        print("关闭文件")
except:
    print("该文件不存在")
"""

#####自定义异常  raise
# 需求：用户名不符合规则，则报异常（用户输入用户名，若用户名不包含字母和数字，则报错，即抛出自定义异常，并捕获该异常）


#1.自定义异常类，继承Exception

class Error(Exception):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"用户名{self.name}不包含字母和数字,用户名要包含字母和数字"
def user():
    try:
        name1 = input("请输入用户名")
        if name1.isdigit() or name1.isalpha() is True or name1.isspace() is True:
            raise Error(name1)
    except Exception as msg:
        print(msg)
    else:
        print("用户名输入完成")
user()
