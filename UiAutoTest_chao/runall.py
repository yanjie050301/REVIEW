"""
 -*- coding: utf-8 -*-
 @File  : runall.py
 @Author: yanjie
 @Date  : 2021/6/16 0016
 @功能描述  :框架运行的入口，实现查找用例，运行用例并生成报告，自动清理报告，发送邮件
 @实现步骤：
    1.导包unittest，os、HtmlTestRunner
    2.查找用例，生成测试套件
        2-1unittest.Testlodder内的discover方法

    3.运行测试用例，并生成报告
        3-1HtmlTestRunner runner.run(suite)
    4.自动清理报告
        4-1autoClear(1-全部清除2-留下最新的5个报告)
"""
import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
class Runall():
    #查找测试用例
    def suite(self):
        dir_path = os.path.dirname(__file__) + "//testCase"
        suite = unittest.defaultTestLoader.discover(start_dir=dir_path,pattern="*test.py")
        return suite
    def run(self):
        report_path = os.path.dirname(__file__)+"//testReport"
        report_list = os.listdir(report_path)
        num = len(report_list)
        while num>6:   #只留最新的5个报告数据
            os.remove(report_path+"//"+report_list[num-7])
            num = num-1
        suite = self.suite()
        # 用HTMLTestRunner运行测试集合，并生成测试报告
        tf = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())   # 获取当前时间，#####时分秒之间不能用冒号
        report_file = report_path + "//appium测试报告"+tf+".html"   #拼接测试报告路径和时间
        with open(report_file,"wb") as f:
            #生成测试结果-报告
            runner = HTMLTestRunner( stream= f,title="appium测试报告",description="测试情况")
            runner.run(suite)
if __name__ == '__main__':
    r = Runall()
    r.run()