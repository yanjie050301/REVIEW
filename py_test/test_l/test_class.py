"""
 -*- coding: utf-8 -*-
 @File  : test_class.py
 @Author: yanjie
 @Date  : 2021/12/23 6:40 下午
 @功能描述  :pytest练习 类
 @实现步骤：
    1.Test开头的类不能包含"__init__"方法
    2.类里面的方法要与test_开头
    3.所有的package包必须要有__init__.py文件
"""
class TestClasss():
    def test_onr(self):
        x = "this"
        assert "h" in x
    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")  #判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。需要注意的是name要用括号括起来