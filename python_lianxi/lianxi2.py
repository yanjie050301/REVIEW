


###########有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
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




















