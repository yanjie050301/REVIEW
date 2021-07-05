"""
 -*- coding: utf-8 -*-
 @File  : Public.py
 @Author: yanjie
 @Date  : 2021/7/5 0005
 @功能描述  :定义公共方法，框架中使用频率高的代码的集合，例如显示等待，获取文件路径等
 @实现步骤：
    1.
    2.
    3.
"""
import os
class public():
    def getdir(self):
        """
        获取当前文件路径
        :return: 返回当前文件路径
        """
        dir = os.path.dirname(os.path.dirname(__file__))
        return dir


if __name__ == '__main__':
    p = public()
    print(p.getdir())




