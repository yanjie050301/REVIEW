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

for a in range(100,1000):
    b = int(a / 100)
    c = int(a / 10 % 10)
    d = int(a % 10)
    if a == b**3 + c ** 3 +d**3:
        print(a)





