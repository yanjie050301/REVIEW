"""
 -*- coding: utf-8 -*-
 @File  : configEmail.py
 @Author: yanjie
 @Date  : 2021/6/16 0016
 @功能描述  :发送邮件配置
 @实现步骤：
    1.
    2.
    3.
"""
import smtplib
import time,os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from UiAutoTest_chao.common.readconfig import ReadConfig
class CinfigEmail():
    def __init__(self):
        c = ReadConfig()
        # 1.配置邮件属性
        self.sender = c.reademail("sender")  # 发件人邮箱
        self.receiver = c.reademail("receiver")  # 接收人邮箱
        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())  # 发送邮件的时间
        self.titel = "appium测试结果——" + t  # 拼接邮件的标题
        self.smtpserver = c.reademail("smtpserver")  # 发送邮箱的服务器
        self.username = c.reademail("username")  # 登录邮箱的用户名
        # 注意：如果邮箱从未开启过pop3/smtp服务，则需要进入邮箱设置开启，开启成功后会提示一个授权码，把此处的密码替换为生成的授权码即可
        self.password = c.reademail("password")  # 登录邮箱的授权码
    def email(self):
        # 2.组装邮件内容和标题
        #查找附件
        dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\testReport"
        dir_list = os.listdir(dir_path)
        report_file = dir_list[len(dir_list)-1]
        # 拼接最新的测试报告路径
        with open(report_file,"rb") as f:
            # 添加附件
            email_body = f.read()
            self.msg = MIMEMultipart("alternative")
            # 第二步：组装邮件内容和标题，
            content = "appium自动化报告发送。。。"
            msgtext = MIMEText(content,"plain","utf-8")
            # 将文本内容加载到msg中
            self.msg.attach(msgtext)
            att = MIMEText(email_body,"plain","utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename=report.html'
            # 将邮件加载到msg中
            self.msg.attach(att)
            self.msg["Subject"] = Header(self.titel, "utf-8")
            self.msg["From"] = self.sender
            self.msg["To"] = self.receiver
    def sendemail(self):
        self.email()
        try:
            #实例化
            s = smtplib.SMTP()
            #连接服务器
            s.connect(self.smtpserver)
            #登录邮箱
            s.login(user=self.username,password=self.password)
            #设置发送人收件人等信息
            s.sendmail(from_addr=self.sender,to_addrs=self.receiver,msg=self.msg.as_string())
        except Exception as mas:
            print("邮件发送失败")
        else:
            print("发送成功")
        finally:
            print("邮件发送完毕")
if __name__ == '__main__':
    e = CinfigEmail()
    e.sendemail()










