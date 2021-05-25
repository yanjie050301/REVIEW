"""
功能描述：
1.加载测试用例
2.运行测试用例
3.生成测试结果-报告
4.发送邮件
"""
import os,unittest,time
from HTMLTestRunner import HTMLTestRunner
from WanAndroid.common.emailconfig import Emailcon

class Runall():
    # 1.加载测试用例
    def createTestSutie(self):
        case_dir = os.path.dirname(os.path.dirname(__file__)) + "//TestCase"   #获取测试用例路径
        sutie = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="Test*.py")  #查找所以以Test开头的测试用例
        return sutie
    # 2.运行测试用例
    def runcase(self):
    # 判断report文件夹里是否有之前的报告，有的话则删除，生成最新的
        report_dir = os.path.dirname(os.path.dirname(__file__)) + "//TestReport" #获取存放测试报告的路径
        list = os.listdir(report_dir)
        for file in list:
            if "report" in file:
                os.remove(report_dir+"//"+file)
        suitie = self.createTestSutie()  #加载测试用例
        # 用HTMLTestRunner运行测试集合，并生成测试报告
        file_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())  #获取生成报告的当前时间
        report_name = report_dir+"//"+file_time+"report.html"  #拼接生成的测试报告的路径及报告的名称
        with open(report_name,"wb") as fp:
            #3.生成测试结果-报告
            runner = HTMLTestRunner(stream=fp, title="接口自动化测试报告", description="测试情况")    #实例化
            runner.run(suitie)
        #发送邮件
        e = Emailcon()
        e.sendemail()
if __name__ == '__main__':
    c = Runall()
    c.runcase()
