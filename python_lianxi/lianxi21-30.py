"""
****************二十一、题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
思想：
"""
"""
list = [1,2]
for n in range(0,20):
    a = list[n] + list[n+1]
    list.append(a)
# print(list)
sum = 0
for m in range(0,20):
    x = list[m]
    y = list[m+1]
    sum = y/x +sum
print(sum)
"""
"""
****************二十二、求1+2!+3!+...+20!的和。
思想：
"""
"""
sum = 0
cheng = 1
for i in range(1,21):
    cheng = cheng*i
    sum = sum + cheng
print(sum)
"""
"""
****************二十三、利用递归方法求5!。
思想：
1.递归自己调用自己
2.要有if-else判断，有个终止的条件
3.累计的时候结果只能return，不能print
"""
"""
def cheng(num):
    sum = 0
    if num ==0:
        sum = 1
    else:
        sum = num * cheng(num-1)
    return sum
print(cheng(5))
"""
"""
****************二十三、利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
思想：
1.递归自己调用自己
2.要有if-else判断，有个终止的条件
3.调用自己的话要有个递减的条件
"""
"""
def out(s,l):
    if l==0:
        return
    else:
        print(s[l-1])
        out(s, l-1)
s = "asdfg"
l = len(s)
out(s,l)
"""
"""
****************二十四、有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
思想：
1.递归
"""
"""
def people(num):
    if num == 1:
        f = 10
    else:
        f = people(num-1)+2
    return f


print(people(5))
"""
"""
****************二十五、给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
思想：
1.分解数字
"""
"""
def num(n):
    l = str(n)
    if len(l) >5 or n <=0:
        print("请输入不多于5位的正整数")
    elif len(l) == 5:
        print(f"该数字为{len(l)}位数")
        yi = int(n/10000)
        er = int(n%10000/1000)
        san = int(n%1000/100)
        si = int(n%100/10)
        wu = n%10
        print("逆序打印为：",wu,si,san,er,yi)
    elif len(l) == 4:
        print(f"该数字为{len(l)}位数")
        er = int(n%10000/1000)
        san = int(n%1000/100)
        si = int(n%100/10)
        wu = n%10
        print("逆序打印为：",wu,si,san,er)
    elif len(l) == 3:
        print(f"该数字为{len(l)}位数")
        san = int(n % 1000 / 100)
        si = int(n % 100 / 10)
        wu = n % 10
        print("逆序打印为：", wu, si, san)
    elif len(l) == 2:
        print(f"该数字为{len(l)}位数")
        si = int(n % 100 / 10)
        wu = n % 10
        print("逆序打印为：", wu, si)
    elif len(l) == 1:
        print(f"该数字为{len(l)}位数")
        print("逆序打印为：",n)
num(4)
"""
"""
****************二十六、一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
思想：
无
"""
"""
def num(n):
    l = str(n)
    if len(l) !=5:
        print("请输入5位的正整数")
    elif len(l) == 5:
        yi = int(n/10000)
        er = int(n%10000/1000)
        san = int(n%1000/100)
        si = int(n%100/10)
        wu = n%10
        if yi == wu and er == si:
            print("该数字为回文数")
        else:
            print("该数字不是回文数")

num(45554)
"""
"""
****************二十七、对10个数进行排序。
思想：
冒泡排序
"""
"""
li = [4,56,3,58,62,41,23,5,78,9]
le = len(li)
for a in range(0,le):
    for b in range(0,le-a-1):
        if li[b]>li[b+1]:
            c = li[b]
            li[b] = li[b+1]
            li[b+1] = c
print(li)
"""
"""
****************二十八、有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
思想：
"""
"""
li = [3,5,9,11,25,36,0]
num = int(input("请输入一个数："))
def paixu(num):
    for a in range(0,len(li)):
        if li[a]>num:
            temp = li[a]
            li[a] = num
            for b in range(a+1,len(li)):
                temp2 = li[b]
                li[b] = temp
                temp = temp2
            break
    print(li)
paixu(num)
"""
"""
****************二十九、将一个数组逆序输出。
思想：
"""
"""
li = [1,2,3,4,5]
#第一种方法
# print(li[::-1])
#第二种方法
li1=[]
l = len(li) -1
while l>=0:
    b = li[l]
    li1.append(b)
    l -=1
print(li1)
"""
"""
****************三十、两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
思想：
"""
x = [
    [12,7,3],
    [4 ,5,6],
    [7 ,8,9]
    ]

y = [
    [5,8,1],
    [6,7,3],
    [4,5,9]
    ]
z = []
for n in range(3):
    a = []
    for m in range(3):
        sum = x[n][m]+y[n][m]
        a.append(sum)
    z.append(a)
print(z)























