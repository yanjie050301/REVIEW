"""
功能说明
    1.记录脚本运行之间的log输出
    2.也可以记录调试的信息
    3.log的级别：
        CRITICAL    严重
        ERROR       错误
        WARNING     警告
        INFO        信息
        DEBUG       调试
"""
import logging,os
def Logconfig():
    path = os.path.dirname(os.path.dirname(__file__)) + "//Log//log.txt"    #拼接存放log文件和地址
    logging.basicConfig(filename=path,filemode="w",level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")

    logger = logging.getLogger("log_test")
    return logger
if __name__ == '__main__':
    a = Logconfig()
    a.info("验s食道反流是甲方证")



