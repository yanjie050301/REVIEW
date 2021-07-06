"""
 -*- coding: utf-8 -*-
 @File  : lianxi41-50.py
 @Author: yanjie
 @Date  : 2021/7/1 0001
 @功能描述  :python练习题
 @实现步骤：
    1.
    2.
    3.
"""
"""
****************四十一、某个公司采用公用电话传递数据，数据是四位的整数，
在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
思想：
"""
"""
def num(num):
    li = []
    num = str(num)
    l = len(num)
    if l !=4 or num.isdigit() is False:       #判断是否是四位数
        print("输入错误，请输入4位整数!")
    else:
        num = int(num)
        first = int(num/1000)   #将4位数分别提取出来存入列表中
        li.append(first)
        s = int(num%1000/100)
        li.append(s)
        t = int(num%100/10)
        li.append(t)
        f = num%10
        li.append(f)
        lii = []
        for a in li:     #每个数字+5后除以10的余数存入列表
            n = a+5
            m = n%10
            lii.append(m)
        # print(lii)
        lii[0],lii[3] = lii[3],lii[0]    #第一位和第四位交换，第二位和第三位交换
        lii[1], lii[2] = lii[2], lii[1]
        print("加密后的数字为：",end="")
        for b in lii:           #遍历后打印
            print(b,end="")
if __name__ == '__main__':
    number = input("请输入4位整数：")
    num(number)
"""
"""
****************四十二、从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
思想：
"""
"""第一种方法"""
"""
name = input("请输入文件名：")
f = open(name+".txt","w",encoding="utf-8")
while True:
    s = input("请输入要写入磁盘的字符：")
    if s == "#":
        print("退出磁盘")
        break
    f.write(s)
f.close()
"""
"""第二种方法"""
"""
name = input("请输入文件名：")
with open(name+".txt","w",encoding="utf-8") as f:
    while True:
        s = input("请输入要写入磁盘的字符：")
        if s == "#":
            print("退出磁盘")
            break
        f.write(s)
"""
"""
****************四十三、从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
思想：
"""

def sinput():
    s = input("请输入一个字符串：")
    a = s.upper()
    print(f"转化为大写字母后为：{a}")
    with open("test.txt","w",encoding="utf-8") as f:
        f.write(a)
    print("写入磁盘成功！")

if __name__ == '__main__':
   sinput()




























