"""
****************十一、古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
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

