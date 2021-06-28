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
"""
def long(s):
    return f"该字符串长度为:{len(s)}"
if __name__ == '__main__':
    s = input("输入一个字符串:")
    print(long(s))
"""
"""
****************三十六、创建一个链表。
思想：
"""
"""
l = []
for i in range(5):
    a = input("input:")
    l.append(a)
print(l)
"""
"""
****************三十七、题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
思想：
"""
"""
def oushu(num):
    i = int(num/2)
    sum = 0
    for n in range(1,i+1):
        sum = 1/(n*2) +sum
    return sum
def jishu(num):
    i = int(num/2+1)
    sum = 0
    for n in range(1,i+1):
        sum = 1/(n*2-1)+sum
    return sum
def count(num):
    if num%2==0:
        sum = oushu(num)
        return f"您输入的数字为偶数，和为：{sum}"
    else:
        sum = jishu(num)
        return f"您输入的数字为奇数，和为：{sum}"
def a():
    try:
        num = int(input("请输入一个正整数："))
    except Exception as msg:
        if msg != "":
            a()
    else:
        if num >0:
            print(count(num))
        else:
            a()
if __name__ == '__main__':
     a()
"""
"""
****************三十八、海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
思想：
"""
"""
i = 0
j = 1
x = 0
while (i < 5) :
    x = 4 * j
    for i in range(0,5) :
        if(x%4 != 0) :
            break
        else :
            i += 1
        x = (x/4) * 5 +1
    j += 1
print(x)
"""
"""
****************三十九、809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
思想：
"""
"""
for s in range(10,100):
    if len(str(s*809))==4 and len(str(s*8))==2 and len(str(s*9))==3 and 809*s==800*s+9*s:
        print(f"??为{s},809*??={809*s}")
"""


































