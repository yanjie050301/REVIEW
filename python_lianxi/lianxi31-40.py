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
****************三十四、有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
思想：
"""
"""
x = input("请输入一个整数列表，使用逗号间隔：")
li = x.split(",")
l = []
for c in range(len(li)):
    i = int(li[c])
    l.append(i)
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
"""
****************三十四、有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
思想：俗名：猴子选大王
"""
"""
n = int(input('请输入总人数:'))
l = []
for i in range(n):
    l.append(i + 1)    #将输入的数字从1开始+1添加到列表中
b = 0
a = 0
e = 0
while e < len(l) - 1:   #判断条件，标记为0就少一个数，最终列表只留下一个数
    if l[a] != 0:   #判断条件，数字为0的不参与报数
        b = b + 1
    if b == 3:
        l[a] = 0  #判断条件，每数到3就会将列表的数字标记为0，
        b = 0
        e = e+1   #每标记为0，就意味着删除一个数，删掉的总数+1，
    a = a + 1
    if a == len(l):    #判断条件，当循环+1长度为列表总长度时，变量a重新赋值为0，再次循环
        a = 0
for c in range(len(l)):
    if l[c] != 0:    #遍历列表找出唯一一个不为0的数字并打印
        print(l[c])
        break
"""
"""
****************三十五、写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
思想：
"""

def long(s):
    return f"该字符串长度为:{len(s)}"
if __name__ == '__main__':
    s = input("输入一个字符串:")
    print(long(s))





