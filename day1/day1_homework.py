import random
# 1.石头剪刀布游戏
# 1：石头2：剪刀3：布
'''
man = random.randint(1,3)
computer = random.randint(1,3)
print(man,computer)
if man==1 and computer==2 or man==2 and computer==3 or man==3 and computer==1:
    print("人胜利")
elif man==computer:
    print("平局")
else:
    print("电脑胜利")
'''
# 2.1-100的累加和
'''
a = 1
b = 0
while a<101:
    b = b + a
    a=a+1
    print(b)
'''
# 3.计算1-100偶数累加和
'''
a = 1
b = 0
while a<101:
    if a%2==0:
        b = b+a
        print(b)
    a = a+1
'''
# 4.计算1-100奇数累加和
'''
a = 1
b = 0
while a<101:
    if a%2==1:
        b = b+a
        print(b)
    a = a+1
'''
# 5.打印星号(正方形)
'''
b = 1
while b<6:
    a = 1
    # 打印一行星星
    while a<6:
        print("*",end="")
        a = a+1
    print("")
    b = b+1
'''
#6. 打印星号(三角形）
# 第一种方法：
'''
a = 1
while a<6:
    print("*"*a)
    a = a+1
'''
# 第二种方法：
'''
a = 1
while a<5:
    b = 0
    while b<a:
        print("*", end="")
        b = b+1
    print()
    a = a+1
'''
#7. 打印星号(正三角)

n = 1   #表示行
w = int(input("请输入行数："))
while n<w+1:
    m = w-1 # 表示列
    while m>=n:
        print(" ", end="")
        m = m-1
    l = 1
    while l<=n:
        print("*",end=" ")
        l = l+1
    print()
    n = n+1

#8. 打印星号(倒三角)
'''
n = 4
while n>0:
    l = 4
    while l>=n:
        print(" ", end="")
        l = l-1
    m = 1
    while m<=n:
        print("*",end=" ")
        m = m+1

    print()
    n = n-1
'''
#9. 打印星号(菱形)
'''
n = 1   #表示行
w = int(input("请输入行数："))
q = (w+1)/2
if w%2==1:
    while n<q+1:
        m = q-1 # 表示列
        while m>=n:
            print(" ", end="")
            m = m-1
        l = 1
        while l<=n:
            print("*",end=" ")
            l = l+1
        print()
        n = n+1
    a = (w-1)/2
    while a>0:
        c = (w-3)/2
        while c>=a:
            print(" ", end="")
            c = c-1
        b = 1
        while b<=a:
            print(" *",end="")
            b = b+1

        print()
        a = a-1
else:
    print("请输入奇数！！！")
'''
#10. 打印九九乘法表
'''
n = 1
while n<10:
    m = 1
    while m<=n:
        print("%d"%n,"*","%d"%m,"=",n*m,end="   ")
        m = m+1
    print()
    n = n+1
'''

# 作业：
# 1.输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
'''
num = int(input("请输入您的成绩："))
if num>100 or num<0:
    print("请输入正确的成绩")
else:
    if 100>=num>=90:
        print("成绩为优")
    elif 90>num>=80:
        print("成绩为良")
    elif 80>num>=70:
        print("成绩为好")
    elif 70>num>=60:
        print("成绩为及格")
    else:
        print("成绩不及格")
'''
# 2.定义一个列表，从键盘输入一个随机数，判断该数是否在列表中
'''
list = (1,23,55,8,9,6,4,7,53)
num = int(input("请输入一个数："))
if num in list:
    print("该数字已存在列表中")
else:
    print("该数字不存在列表中")
'''

# 预习循环后的作业：
# 3、求10阶乘
# 4、求100以内能被3整除的数，并将作为列表输出
# 5、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# 6、求斐波那契数列 1 2 3 5 8 13 ……
# 7、求10000以内的质数