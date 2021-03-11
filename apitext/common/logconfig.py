"""
功能介绍：
    1.记录脚本运行之间的log输出
    2.也可以记录调试的信息
    3.log的级别：
        CRITICAL    严重
        ERROR       错误
        WARNING     警告
        INFO        信息
        DEBUG       调试
"""
#**************1.导入日志所需要的包
import logging,os
def log():
    log_dir = os.path.dirname(os.path.dirname(__file__)) + "\\Log\\log.text"
    #*************2.设置log基础配置信息（级别level，格式format）,filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
   #a是追加模式，默认如果不写的话，就是追加模式
    logging.basicConfig(filename=log_dir,filemode="w",level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        #*************3.定义日志名称，在输出日志时候显示
    logger = logging.getLogger("log_test")
    return logger
if __name__ == '__main__':
    logger = log()
    logger.info("info信fff息哦")
    logger.error("error信息")