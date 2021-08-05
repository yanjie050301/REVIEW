"""
 -*- coding: utf-8 -*-
 @File  : b.py
 @Author: yanjie
 @Date  : 2021/8/4 0004
 @功能描述  :
 @实现步骤：
    1.
    2.
    3.
"""

import wx,xlrd
import os


class SiteLog(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id, title='天章财务私人定制', size=(640, 480))
        panel = wx.Panel(self)
        box = wx.TextEntryDialog(None, '请输入和值', '天章财务私人定制',)
        if box.ShowModal() == wx.ID_OK:  # 如果你点击了ok 我才会存储这个打进去的数值
            answer = box.GetValue()
        self.sum = float(answer)
        self.SelBtn = wx.Button(self, label='导入数据', pos=(305, 5), size=(80, 25))
        self.SelBtn.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        self.OkBtn = wx.Button(self, label='提交', pos=(405, 5), size=(80, 25))
        self.OkBtn.Bind(wx.EVT_BUTTON, self.output)
        self.FileName = wx.TextCtrl(self, pos=(5, 5), size=(230, 25))
        self.FileContent = wx.TextCtrl(self, pos=(5, 35), size=(620, 480), style=(wx.TE_MULTILINE))

    def OnOpenFile(self, event):    #上传文件
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard)
        if dialog.ShowModal() == wx.ID_OK:
            self.FileName.SetValue(dialog.GetPath())
            dialog.Destroy()
    def ReadFile(self):
        file = self.FileName.GetValue()
        e = xlrd.open_workbook(file)
        sh = e.sheet_by_index(0)
        nrow = sh.nrows
        li = []
        for n in range(1, nrow):
            num = sh.cell_value(n, 2)
            li.append(num)
        return li
    def two_num(self):
        li = self.ReadFile()
        for l in range(0,len(li)):
            a = float(li[l])
            for m in range(l+1,len(li)):
                b = float(li[m])
                if round(a + b,2) == self.sum:
                    return f"您输入的和值为{self.sum}，加数为{a}和{b}"
                    break

    def three_num(self):
        li = self.ReadFile()
        for q in range(0,len(li)):
            c = float(li[q])
            for w in range(q+1,len(li)):
                d = float(li[w])
                for r in range(w+1,len(li)):
                    e = float(li[r])
                    if round(c + d + e,2) ==  self.sum:
                        return f"您输入的和值为{self.sum}，加数为{c}、{d}、{e}"
                        break
    def four_num(self):
        li = self.ReadFile()
        for q in range(0,len(li)):
            c = float(li[q])
            for w in range(q+1,len(li)):
                d = float(li[w])
                for r in range(w+1,len(li)):
                    e = float(li[r])
                    for t in range(r+1,len(li)):
                        f = float(li[t])
                        if round(c + d + e + f,2) == self.sum:
                            return f"您输入的和值为{self.sum}，加数为{c}、{d}、{e}、{f}"
                            break
    def five_num(self):
        li = self.ReadFile()
        for q in range(0, len(li)):
            c = float(li[q])
            for w in range(q + 1,len(li)):
                d = float(li[w])
                for r in range(w + 1, len(li)):
                    e = float(li[r])
                    for t in range(r + 1, len(li)):
                        f = float(li[t])
                        for y in range(t + 1, len(li)):
                            g = float(li[y])
                            if round(c + d + e + f + g,2) == self.sum:
                                return f"您输入的和值为{self.sum}，加数为{c}、{d}、{e}、{f}、{g}"
                                break

    def count(self):
        if self.two_num() is not None:
           return self.two_num()

        elif self.three_num() is not None:
            return self.three_num()

        elif self.four_num() is not None:
            return self.four_num()

        elif self.five_num() is not None:
            return self.five_num()

        else:
            return f"您输入的和值为{self.sum}，无加数"

    def output(self,event):
        jkl = self.count()
        self.FileContent.SetValue(jkl)
if __name__ == '__main__':
    app = wx.App()
    SiteFrame = SiteLog(parent=None, id=-1)
    SiteFrame.Show()
    app.MainLoop()
