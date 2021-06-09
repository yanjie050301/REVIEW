"""
****************三十一、题目：统计 1 到 100 之和。
思想：
"""
"""
a =0
for n in range(101):
    a = a+n
print(a)
"""
"""
def sum(a):
    s = 0
    if a <0:
        return 0
    else:
        s = a+sum(a-1)
        return s
print(sum(100))
"""
"""
****************三十二、输入3个数a,b,c，按大小顺序输出。
思想：
"""
"""
a = int(input("num1:"))
b = int(input("num2:"))
c = int(input("num3:"))
if a>b and a>c:
    print(a,end=" ,")
    if b>c:
        print(b,end=" ,")
        print(c)
    else:
        print(c,end=" ,")
        print(b)
elif b>a and b>c:
    print(b,end=" ,")
    if a>c:
        print(a,end=" ,")
        print(c)
    else:
        print(c,end=" ,")
        print(a)
elif c>a and c>b:
    print(c, end=" ,")
    if b > a:
        print(b, end=" ,")
        print(a)
    else:
        print(a, end=" ,")
        print(b)
"""
"""
l = []
a = int(input("num1:"))
l.append(a)
b = int(input("num2:"))
l.append(b)
c = int(input("num3:"))
l.append(c)
m = max(l)
n = min(l)
for h in range(0,3):
    if l[h]!=m and l[h]!=n:
        q = l[h]
print(m,q,n)

"""
"""
****************三十三、输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
思想：
"""
"""
l = [45,2,5,63,25,48,55]
m = max(l)
n = min(l)
for a in range(len(l)):
    if l[a]==m:
        i = l[0]
        l[0] =l[a]
        l[a]=i
    if l[a]==n:
        i = l[len(l)-1]
        l[len(l)-1] =l[a]
        l[a]=i

print(l)
"""
"""
****************三十三、有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
思想：
"""
"""
l = [1,2,3,4,5]
num = int(input("请输入向后移动几位："))
def houyi(num):
    if num>=len(l) or num <=0:
        return "输入的数字小于0或大于列表长度，请输入正确的数字"
    else:
        print(f"移动前列表为{l}")
        for a in range(num):
            b = len(l)-1
            item = l[b]
            while b >=0:
                l[b] = l[b-1]
                b = b-1
            l[0] = item
        return f"移动后列表为{l}"
print(houyi(num))
"""

















