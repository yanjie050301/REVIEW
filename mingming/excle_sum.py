"""
 -*- coding: utf-8 -*-
 @File  : excle_sum.py
 @Author: yanjie
 @Date  : 2021/7/30 0030
 @功能描述  :
 @实现步骤：
    1.
    2.
    3.
"""
"""
import xlrd
e = xlrd.open_workbook("汇总.xls")
sh = e.sheet_by_index(0)
now = sh.nrows
# num = sh.cell_value(1,2)
# nu=sh.cell_value(2,2)
li = []
sets = set()
for n in range(1,now):
    num = sh.cell_value(n,2)
    li.append(num)
# print(li)
"""
li = [2.3,5,2,3.6,5.6,8,7.9]
sum = float(17.3)
for l in range(0,len(li)):
    a = float(li[l])
    for m in range(l+1,len(li)):
        b = float(li[m])
        if a + b == sum:
            print(a, "eeee", b)
            break
for q in range(0,len(li)):
    c = float(li[q])
    for w in range(q+1,len(li)):
        d = float(li[w])
        for r in range(w+1,len(li)):
            e = float(li[r])
            if c + d + e == sum:
                print(c, "eeee", d, "eeee", e)
                break
for q in range(0,len(li)):
    c = float(li[q])
    for w in range(q+1,len(li)):
        d = float(li[w])
        for r in range(w+1,len(li)):
            e = float(li[r])
            for t in range(r+1,len(li)):
                f = float(li[t])
                print(type(c + d + e + f))
            if c + d + e + f == sum:
                print(c, "eeee", d, "eeee", e, "eeee", f)
                break
                # li = [2.3, 5, 2, 3.6, 5.6, 8, 7.9]
#     c = float(c)
#     for d in li:
#         d = float(d)
#         for e in li:
#             e = float(e)
#             for f in li:
#                 f = float(f)
#                 for g in li:
#                     g = float(g)
#                     if c + d + e + f + g == sum:
#                         sets.add(e)
#                         sets.add(d)
#                         sets.add(c)
#                         sets.add(f)
#                         sets.add(g)
# print(sets)