"""
 -*- coding: utf-8 -*-
 @File  : test_sample.py.py
 @Author: yanjie
 @Date  : 2021/12/23 6:27 下午
 @功能描述  :简单的一个pytest练习
 @注意点：
    1.文件夹必须以*_test或test_*开头
    2.函数要test_*开头
    3.
"""
x = 3
def func(x):
    return x+1
def test_answer():
    assert func(3) ==5