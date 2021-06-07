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





























