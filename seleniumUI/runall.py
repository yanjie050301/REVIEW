"""
 -*- coding: utf-8 -*-
 @File  : runall.py
 @Author: yanjie
 @Date  : 2021/7/13 0013
 @功能描述  :
 @实现步骤：
    1.
    2.
    3.
"""
import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from UiAutoTest_chao.common.configEmail import CinfigEmail
from seleniumUI.common.Public import public
class Runall():
    p = public()
    #查找测试用例
    def suite(self):

        dir_path = self.p.getdir() + "//testCase"
        suite = unittest.defaultTestLoader.discover(start_dir=dir_path,pattern="*test.py")
        return suite
    def run(self):
        """筛选报告"""
        report_path = self.p.getdir()+"//testReport"
        report_list = os.listdir(report_path)
        num = len(report_list)
        while num>1:   #只留最新的一组报告
            os.remove(report_path+"//"+report_list[num-1])
            num = num-1
        suite = self.suite()
        # 用HTMLTestRunner运行测试集合，并生成测试报告
        tf = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())   # 获取当前时间，#####时分秒之间不能用冒号
        report_file = report_path + "//selenium测试报告"+tf+".html"   #拼接测试报告路径和时间
        with open(report_file,"wb") as f:
            #生成测试结果-报告
            runner = HTMLTestRunner( stream= f,title="selenium测试报告",description="测试情况")
            runner.run(suite)
        ce = CinfigEmail()   #发送邮件
        ce.sendemail()
if __name__ == '__main__':
    r = Runall()
    print(r.suite())