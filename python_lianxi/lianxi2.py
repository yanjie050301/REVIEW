
"""
************有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

li = []
for i in range(1,5):
    i = str(i)
    for n in range(1,5):
        n = str(n)
        for m in range(1,5):
            m = str(m)
            if i==n or i==m or n==m:
                continue
            num = i+n+m
            li.append(num)
print(li)
"""
"""
*****************
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""
"""
i = float(input("请输入您的利润(单位：万元)："))
l1 = [10,10,20,20,40]
l2 = []    #存放减掉后的数
l3 = [0.1,0.075,0.05,0.03,0.015,0.01]
if i <10:
    print(f"您的利润为{i*0.1}万元")
else:
    for a in range(1, 7):
        for b in l1:
            i = i-b
            if i < 0:
                break
            l2.append(i)
    lens = len(l2)
    j = 0
    for n in range(0,lens):
        j = l1[n]*l3[n] + j
    z = l2[lens-1] * l3[lens] +j
    print("您的利润为","%.4f" % z ,"万元")
"""

i = float(input('净利润:'))
# i = 10.7
arr = [100,60,40,20,10,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print (r)



















