"""
 -*- coding: utf-8 -*-
 @File  : pytest_order.py
 @Author: yanjie
 @Date  : 2021/12/24 11:43 上午
 @功能描述  :使用pytest-prder控制用例执行的顺序
 @实现步骤：
    1.
    2.
    3.
"""
import pytest
import pytest_ordering
@pytest.mark.run(order =2 )
def test_one():
    print("用例1")
    assert True
@pytest.mark.run(order =3)
def test_two():
    print("用例2")
    assert True
@pytest.mark.run(order = 1)
def test_three():
    print("用例3")
    assert True