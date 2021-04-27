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
