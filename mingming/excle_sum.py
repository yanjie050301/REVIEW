"""
 -*- coding: utf-8 -*-
 @File  : excle_sum.py
 @Author: yanjie
 @Date  : 2021/7/30 0030
 @功能描述  :给一个和值，要求找出表格中哪几个数相加的
 @实现步骤：
    1.
    2.
    3.
"""

import xlrd
class Calculate():
    def __init__(self,file):

        e = xlrd.open_workbook(file)
        self.sh = e.sheet_by_index(0)
        self.nrow = self.sh.nrows
        self.li = []
        sum = float(1147.7)
        for n in range(1,self.nrow):
            num = self.sh.cell_value(n,2)
            self.li.append(num)
    def two_num(self,sum):
        for l in range(0,len(self.li)):
            a = float(self.li[l])
            for m in range(l+1,len(self.li)):
                b = float(self.li[m])
                if round(a + b,2) == sum:
                    return f"您输入的和值为{sum}，加数为{a}和{b}"
                    break
    def three_num(self,sum):
        for q in range(0,len(self.li)):
            c = float(self.li[q])
            for w in range(q+1,len(self.li)):
                d = float(self.li[w])
                for r in range(w+1,len(self.li)):
                    e = float(self.li[r])
                    if round(c + d + e,2) == sum:
                        return f"您输入的和值为{sum}，加数为{c}、{d}、{e}"
                        break
    def four_num(self,sum):
        for q in range(0,len(self.li)):
            c = float(self.li[q])
            for w in range(q+1,len(self.li)):
                d = float(self.li[w])
                for r in range(w+1,len(self.li)):
                    e = float(self.li[r])
                    for t in range(r+1,len(self.li)):
                        f = float(self.li[t])
                        if round(c + d + e + f,2) == sum:
                            return f"您输入的和值为{sum}，加数为{c}、{d}、{e}、{f}"
                            break
    def five_num(self,sum):
        for q in range(0, len(self.li)):
            c = float(self.li[q])
            for w in range(q + 1,len(self.li)):
                d = float(self.li[w])
                for r in range(w + 1, len(self.li)):
                    e = float(self.li[r])
                    for t in range(r + 1, len(self.li)):
                        f = float(self.li[t])
                        for y in range(t + 1, len(self.li)):
                            g = float(self.li[y])
                            if round(c + d + e + f + g,2) == sum:
                                return f"您输入的和值为{sum}，加数为{c}、{d}、{e}、{f}、{g}"
                                break

    def count(self,sum):
        if self.two_num(sum) is not None:
            return self.two_num(sum)
        elif self.three_num(sum) is not None:
            return self.three_num(sum)
        elif self.four_num(sum) is not None:
            return self.four_num(sum)
        elif self.five_num(sum) is not None:
            return self.five_num(sum)
        else:
            return f"您输入的和值为{sum}，无加数"
if __name__ == '__main__':
    c = Calculate("汇总.xls")
    print(c.count(101.8))
    # print(c.count(578))