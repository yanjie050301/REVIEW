#1. 有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转
str = "welocme to super&Test"
str1 = []
a =len(str)-1
while a>=0:     #将字符串倒叙添加到列表中
    str1.append(str[a])
    a = a-1
print(str1)
c = ""
for b in str1:    #遍历列表
    c = c+b        #拼接成字符串
print(c)
d = c.split(" ")  #以 分割字符串，并命名为d列表
e = len(d)-1
while e>=0:      #倒叙获取列表，并已字符串的形式打印
    print(d[e],end=" ")
    e = e-1
# 2.当前文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
# lucy:21，tom:30
# xiaoming:18，xiaohong:15
# xiaowang:20，xiaohei:19
# 请输出年龄大于18岁的人名

# 将内容resdline一行一行读出来
# 使用split拆分开
# 组成字典
# 将字典values遍历
# 判断是否大于18岁
# 使用get获取keys
# 打印人名
# 3.递归实现斐波那契数列
# 4.debug的快捷键：f8/f7/f9分别的作用