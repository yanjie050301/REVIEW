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
def out(s,l):
    if l==0:
        return
    else:
        print(s[l-1])
        out(s, l-1)
s = "asdfg"
l = len(s)
out(s,l)



























