# 1、PDF中while循环的最后两个题目（1-三角形*）【已完成】
# 2、求100以内能被3整除的数，并将作为列表输出
# list = []
# for a in range(1,101):
#     if a%3==0:
#         list.append(a)
# print(list)
# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
'''#方法一：
list = [1,2,3,4,3,4,2,5,5,8,9,7]
jihe = set()
for a in list:
    jihe.add(a)
list1 = []
for b in jihe:
    list1.append(b)
print(list1)
'''
'''
#方法二
list = [1,2,3,4,3,4,2,5,5,8,9,7]
list1 = []
for a in list:
    if a not in list1:
        list1.append(a)
print(list1)
'''
# 4、求斐波那契数列 1 1 2 3 5 8 13 ……
'''
a =b = 1
list = []
list.append(a)
list.append(b)
w = int(input("请输入斐波那契数列行数："))
n = 0
while n <= w:
    m = list[n] + list[n+1]
    list.append(m)
    n = n+1
print(list)
'''
# 5、求100以内的质数（只能被1和它本身整除）
'''
li = []
for a in range(2,100):
    b = 2
    while b <a:
        if a%b == 0:
            break
        b = b+1
    else:
        li.append(a)
        
print(li)

'''

# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
'''
s1 = "aabbbcddef"
li = []
a = 0
while a < len(s1):     #遍历字符串s1
    b = a+1
    while b<len(s1):      #字符串第一个字符依次和后面字符相比
        if s1[a] == s1[b]:    #若字符相同，则把相同的字符添加到列表li中
            li.append(s1[b])
        b = b+1
    a =a +1
print("相同字符集合为：",li)
lis = list(s1)
print("去重后的字符为：",end="")
for w in lis:    #遍历列表li
    if w not in li:      
        print(w,end="")
'''
# 7、有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
'''
s1 = "welocme to super&Test"
a = s1[11:16:]
b = s1[17::]
print(a+b)
'''
# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
'''
#方法一：
s1 = "welocme to super&Test"
s1 = list(s1)
s1.reverse()
for a in s1:
    print(a,end="")
# print(s1)
'''
#方法二
'''
s1 = "welocme to super&Test"
print(s1[::-1])
'''
# 9、有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
'''
s1 = "abcdef"
print(len(s1))
s2 = list(s1)
l = len(s1)-1
b = []
while l>=0:
    b.append(s1[l])
    l = l-1
print(b)
for a in b:
    print(a,end="")
'''
# 10、有一堆字符串，“aabbbcddef”，输出abcdef
'''
s1 = "aabbbcddef"
list2 = list(s1)     #将字符串转化为列表
list1 = []
for a in list2:
    if a not in list1:
        list1.append(a)
print("去重后的列表为：",list1)
print("去重后的字符为：",end="")
for b in list1:
    print(b,end="")
'''


