
"""
************一、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
"""
for i in range(1,5):
    for n in range(1,5):
        for m in range(1,5):
            if i !=n and n!=m and i!=m:
                print(i,n,m)



"""


"""
*****************二、
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""
"""
import decimal
from decimal import *

getcontext().prec = 3     #控制有效数字
r = Decimal(1) / Decimal(6)
print("rrrr",r)
i = 10.7
i = Decimal.from_float(i)    #浮点数据转换为Decimal类型
print("iiiii",i)

"""
"""
i = float(input("请输入您的利润(单位：万元)："))
l1 = [10,10,20,20,40]
l2 = []    #存放减掉后的数
l3 = [0.1,0.075,0.05,0.03,0.015,0.01]
if i <10:
    print(f"您的奖金为{i*0.1}万元")
else:
    for a in range(1, 7):
        for b in l1:
            i = i-b
            if i < 0:
                break
            # print("iiii",i)
            l2.append(i)
    # print(l2)
    lens = len(l2)
    j = 0
    for n in range(0,lens):
        j = l1[n]*l3[n] + j
    z = l2[lens-1] * l3[lens] +j
    # print(f"您的利润为{z}万元")
    print("您的奖金为","%.4f" % z ,"万元")
"""
"""
i = float(input('净利润:'))
# i = 10.7
arr = [100,60,40,20,10,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print (r)

"""
"""
***********三、输入某年某月某日，判断这一天是这一年的第几天？
"""

"""
class Ymd():
    def __init__(self,month,year,day):
        self.year = year
        self.month = month
        self.day = day
        self.month_31 = [1,3,5,7,8,10,12]
        self.month_30 = [4,6,9,11]
    def ping(self):
        date = 0
        if self.month > 2:
            for a in self.month_31:
                if a<self.month:
                    date = date+31
            for b in self.month_30:
                if b <self.month:
                    date = date + 30
            date = date + self.day +28
            return date
        elif self.month == 2:
            date = self.day + 31
            return date
        elif self.month == 1:
            return self.day
    def run(self):
        num = self.ping() +1
        return num
    def year1(self):
        if self.year %4 ==0 and self.year %100 != 0:
            day_num = self.run()
            print(f'今年是闰年，这一天是这一年的第{day_num}天')
        else:
            day_num = self.ping()
            print(f'今年是平年，这一天是这一年的第{day_num}天')
if __name__ == '__main__':
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日："))
    a = Ymd(month,year,day)
    a.year1()

"""
y = 2000
m = 12
d = 31
def Year(y,m,d):
    sum =0
    for n in range(1,m):#判断月份是31天还是30天
        if n in [1,3,5,7,8,10,12]:
            month = 31
        elif n in [4,6,9,11]:
            month = 30
        else:
            month = 0
        if n ==2:  #判断年份是平年还是闰年，得2月份是多少天
            if y % 4 == 0:
                eryue = 29
            else:
                eryue = 28
        sum = sum + month   #累加整月的天数
    sum = sum + eryue+d   #整月的天数+二月的天数+当月的天数
    return sum
if __name__ == '__main__':
    Year()










"""
****************四、输入三个整数x,y,z，请把这三个数由小到大输出。
"""
"""
x,y,z = input("请输入x,y,z:").split(" ")
x =int(x)
y =int(y)
z =int(z)
list1 = []
list1.append(x)
list1.append(y)
list1.append(z)
# a = 0
# while a<len(list1):
#     b = 0
#     while b <len(list1)-1:
#         if list1[a] < list1[b]:
#             c = list1[a]
#             list1[a] = list1[b]
#             list1[b] = c
#         b += 1
#     a +=1
list1.sort()   #reverse=True  从大到小排序
print(list1)
"""

"""
****************五、斐波那契数列  0 1 1 2 3 5 8 13 21 
"""
"""
list1 = [0,1]
num = int(input("请输入数列个数："))
def num_list(num):
    for a in range(0,num-2):
        b = list1[len(list1)-1] + list1[len(list1)-2]
        list1.append(b)
    print(list1)
num_list(num)
"""
"""
****************六、将一个列表的数据复制到另一个列表中。
"""
"""
ll = [1,2,3,4,5,6,8,8]
# 方法一:
# kk = ll[:]
# print(kk)
# 方法二：
hh = []
hh.extend(ll)
print(hh)
"""
"""
****************七、输出 9*9 乘法口诀表。
"""
"""
def excle():
    for i in range(1,10):
        print()
        for n in range(1,i+1):
            j = i*n
            print(f"{i}*{n}={j}  ",end="")

excle()
"""
"""
****************八、暂停一秒输出。
"""
"""
import time
li = [1,2,3,4,5,6]
def sp():
    for a in li:
        print(a)
        time.sleep(1)
sp()
"""
"""
****************九、暂停一秒输出，并格式化当前时间。
"""
"""
import time
def T():
    tm = time.strftime("%Y:%m:%d:%H:%M:%S",time.localtime(time.time()))
    print(tm)
    time.sleep(2)
    tm1 = time.strftime("%Y:%m:%d:%H:%M:%S", time.localtime(time.time()))
    print(tm1)
T()
"""
















