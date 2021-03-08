"""
功能描述：
1.加载测试用例
2.运行测试用例
3.生成测试结果-报告
4.发送邮件
"""
import os,unittest,time
from HTMLTestRunner import HTMLTestRunner
#1.加载测试用例
def creatTestSutie():
    case_dir = os.path.dirname(os.path.dirname(__file__)) + "//TestCase"
    suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="Test*.py")
    # print(suite)
    return  suite
# 2.运行测试用例

if __name__ == '__main__':
    suite = creatTestSutie()
    #2.用HTMLTestRunner运行测试集合，3.并生成测试报告
    tf = time.strftime("%Y.%m.%d.%H-%M-%S",time.localtime())    #获取当前时间，#####时分秒之间不能用冒号
    report_file = os.path.dirname(os.path.dirname(__file__)) + "/Report/"+ tf +"report.html"    #测试报告的名称及路径
    with open(report_file,"wb") as fp:
        runner = HTMLTestRunner(stream = fp,title = "接口自动化测试报告",description = "测试情况")
        runner.run(suite)



















