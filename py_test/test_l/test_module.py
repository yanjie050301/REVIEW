"""
 -*- coding: utf-8 -*-
 @File  : test_module.py
 @Author: yanjie
 @Date  : 2021/12/24 11:17 上午
 @功能描述  :pytest用例运行级别
 @说明：
    1.从结果可以看出：优先级为setup_module/teardown_module的优先级是最大的，然后函数里面用到的setup_function/teardown_function与类里面的setup_class/teardown_class互不干涉。
    2.
    3.
"""
import pytest
def setup_module():
    print("setup_module:整个.py文件执行前运行一次，初始化测试环境")
def teardown_module():
    print("teardown_module:整个.py文件执行完毕后运行一次，还原测试环境")
def setup_function():   #每个用例都要执行一次
    print("setup_function:每个用例执行前执行一次")
def teardown_function():
    print("teardown_function:每个用例执行后执行一次")
def test_one():
    print("test_one正在执行-----")
    x = "this"
    assert "h" in x
def test_two():
    print("test_two正在执行-----")
    x = "hello"
    assert hasattr(x,"check")

class TestCase():
    def setup_class(self):  #整体用例走完，才执行一次
        print("setup_class:所有用例执行前执行一次")
    def teardown_class(self):
        print("teardown_class:所有用例执行后执行一次")
    def test_three(self):
        print("test_three正在执行-----")
        x = "this"
        assert "h" in x
    def test_four(self):
        print("test_four正在执行-----")
        x = "hello"
        assert "h" in x

if __name__ == '__main__':
    pytest.main(["-s","test_module.py"])




