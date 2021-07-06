"""
 -*- coding: utf-8 -*-
 @File  : SendEmail.py
 @Author: yanjie
 @Date  : 2021/7/5 0005
 @功能描述  :邮箱的相关信息配置
 @实现步骤：
    1.导包smtplib
    2.配置发件人、收件人、登录邮箱等信息配置
        2.1通过readconfig读取配置信息
    3.配置邮箱的附件
        3.1找到脚本自动生成report的路径
        3.2将路径下的文件全部读取出来listdir，结果为一个列表
        3.3遍历列表，找到综合邮件template.html
        3.4拼接成新的文件路径，对该文件进行编辑
    4.配置邮件的标题及内容
        4.1使用MIMEText添加邮件内容
        4.2使用MIMEMultipart添加邮件附件
        4.3
    5.登录邮箱服务器，发送邮件
"""
import smtplib,time,os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from seleniumUI.common.ReadConfig import ReadConfig
from seleniumUI.common.Public import public
from seleniumUI.common.Log import l
class SendEmail():
    def __init__(self):
        """
        读取发件人、收件人、登录邮箱的用户名及密码等信息
        """
        rc = ReadConfig()
        self.sender = rc.getemail("sender")
        self.receiver = rc.getemail("receiver")
        self.smtpserver = rc.getemail("smtpserver")
        self.username = rc.getemail("username")
        self.password = rc.getemail("password")
        t = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        self.title = "SeleniumUI自动化测试" +t    #拼接的邮件标题
    def email(self):
        #查找附件
        p = public()
        path = p.getdir()+"\\TestReport"   #附件测试报告地址
        rlist = os.listdir(path)
        for r in rlist:
            if r == "template.html":
                rfile = r                   #只要综合报告
                break
        # 拼接最新的测试报告路径
        new_path = path + "\\" + rfile
        with open(new_path,"rb") as f:
            #添加附件
            mail_body = f.read()
            self.msg = MIMEMultipart("alternative")
            # **************第二步：组装邮件内容和标题，中文需要参数“utf-8”,单字节字符不需要加参数
            # 在邮件中加入文本内容
            centent = "selenium报告发送中......"
            mimetext = MIMEText(centent,'plain','utf-8')# plain是字体，utf-8是编码方式
            # 将文本内容加载到msg中
            self.msg.attach(mimetext)
            att = MIMEText(mail_body,"plain","utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename=report.html'
            # 将邮件加载到msg中
            self.msg.attach(att)
            self.msg["Subject"] = Header(self.title, "utf-8")
            self.msg["From"] = self.sender
            self.msg["To"] = self.receiver
            l.info("邮件的内容和标题组装成功")
    def sendemail(self):
        self.email()
        try:
            s = smtplib.SMTP() #实例化
            s.connect(self.smtpserver)  #连接服务器
            s.login(self.username,self.password)   #登录邮箱
            s.sendmail(self.sender,self.receiver,self.msg.as_string())   #发送邮件
        except Exception as msg:
            l.info(msg)
        else:
            l.info("邮件发送成功")
if __name__ == '__main__':
    se = SendEmail()
    se.sendemail()










