"""
****************十一、古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
"""
"""
class Rebat():
    def __init__(self,month):
        self.month = month
    def little_r(self):
        a = 1
        b = 1
        if self.month <= 0:
            print("输入错误！")
        elif self.month<3:
            print(f"第{self.month}个月，本月兔子为1对")
        else:
            li_r = [0,1,1]
            for i in range(3,self.month+1):
                c = li_r[i-2] + li_r[i-1]
                li_r.append(c)
            print(f"第{self.month}个月，本月兔子为{c}对")
if __name__ == '__main__':
    n = int(input("请输入月份："))
    a = Rebat(n)
    a.little_r()
"""

"""
****************十二、判断101-200之间有多少个素数，并输出所有素数。
方案：判断素数的方法，一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数
思想：
1.先筛选出来合数
2.判断101-200之间的数是否在合数列表中，不在的即为素数
"""
"""
from math import sqrt
li = []
for i in range(101,200):
    a = int(sqrt(i+1))
    for n in range(2,a+1):
        if i%n == 0:
            # print(i)
            li.append(i)
            break
lii =[]
for b in range(101, 200):
    if b not in li:
        print(b)
        lii.append(b)
print(len(lii))
"""
"""
****************十三、打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
思想：
1.把数字想办法分开，独立的数字
2.判断是否是水仙花数
"""
"""
for a in range(100,1000):
    b = int(a / 100)
    c = int(a / 10 % 10)
    d = int(a % 10)
    if a == b**3 + c ** 3 +d**3:
        print(a)
"""
"""
****************十四、将一个正整数分解质因数。
例如：例如：输入90,打印出90=2*3*3*5。
思想：
能除开就打印，然后把商重新定义为输入的数，再从头循环除
"""
"""
def zhi(num):
    for n in range(2,num+1):
        if num%n == 0:
            print(f"{n}*",end="")
            c = int(num / n)
            if c == 1:
                print("1")
            zhi(c)
            break
num =int(input("请输入一个数："))
if num == 1:
    print("1既不是合数也不是质数")
else:
    print(f'{num} = ',end="")
    zhi(num)
"""
"""
****************十四、数据库读数据，判断学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
思想：
1.连接数据库，依次读取数据，
2.判断数据符合条件，再次输出相应的结果
"""
import mysql.connector
import pymysql
"""
#连接数据库
db = pymysql.connect(host="localhost",user = "root",passwd="123456",db="yanjie")
#获取游标
cursor = db.cursor()
# print(cursor)
#执行数据库语句
cursor.execute("select * from user;")
#获取全部数据库数据
# se = cursor.fetchall()
#获取一条数据
se1 = cursor.fetchone()
print(se1)
#关闭数据库
db.close()
"""
class Datasql():
    def __init__(self):
        #连接数据库
        self.db = pymysql.connect(host="localhost",user = "root",passwd="123456",db="yanjie")
        #创建游标
        self.cursor = self.db.cursor()
        #操作sql语言
        self.cursor.execute("select * from shisi;")
    def chengji(self):
        if course >=90:
            print(f"该学生姓名为{name},成绩为{course}，等级为A")
        elif 60<= course <=89:
            print(f"该学生姓名为{name},成绩为{course}，等级为B")
        elif course<60:
            print(f"该学生姓名为{name},成绩为{course}，等级为C")
    def readdb(self):
        while True:
            #依次读取数据
            se = self.cursor.fetchone()
            if se is None:
                break
            global name,course
            name = se[1]
            course = int(se[2])
            self.chengji()
            # print(type(se[2]))
        self.db.close()
if __name__ == '__main__':
    a = Datasql()
    a.readdb()

