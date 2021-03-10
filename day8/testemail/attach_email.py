"""
发送带有附件的邮件
"""
import os
import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
class SendEmail():
    def __init__(self):
        """
       # 发送内容邮件
       """
        # ***************第一步：配置邮箱属性
        self.sender = "18911032248@163.com"  # 发件人邮箱
        self.receiver = "1353037583@qq.com"  # 接收人邮箱
        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())  # 发送邮件的时间
        # print(t)
        self.titel = "自动化测试结果——" + t  # 拼接邮件的标题
        self.smtpserver = "smtp.163.com"  # 发送邮箱的服务器
        self.username = "18911032248@163.com"  # 登录邮箱的用户名
        # 注意：如果邮箱从未开启过pop3/smtp服务，则需要进入邮箱设置开启，开启成功后会提示一个授权码，把此处的密码替换为生成的授权码即可
        self.password = "IXFQVCYWTXMHQXFO"  # 登录邮箱的授权码
    def sendMail(self):
        # *********发送附件
        #查找附件
       with open("report.txt","rb") as f:
            mail_body = f.read()
            self.msg = MIMEMultipart("alternative")
            #添加附件
            # **************第二步：组装邮件内容和标题，中文需要参数“utf-8”,单字节字符不需要加参数
            #在邮件中加入文本内容
            content = "Python邮件发送测试..."
            msgtext= MIMEText(content,"plain","utf-8")    # plain是字体，utf-8是编码方式
            # 将文本内容加载到msg中
            self.msg.attach(msgtext)
            att = MIMEText(mail_body,"plain","utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename=report5555.txt'
            # 将邮件加载到msg中
            self.msg.attach(att)
            self.msg["Subject"] = Header(self.titel,"utf-8")
            self.msg["From"] = self.sender
            self.msg["To"] = self.receiver
        #*************第三步：登录并发送邮件
       try:
            #实例化SMTP类
            s = smtplib.SMTP()
            #连接smtp服务器
            s.connect(self.smtpserver)
            #登录邮箱
            s.login(self.username,self.password)
            #设置发件人，收件人和邮件内容
            s.sendmail(self.sender,self.receiver,self.msg.as_string())
       except:
            print("邮件发送失败")
       else:
            print("邮件发送成功")
       finally:
            #退出服务器
            s.quit()

if __name__ == '__main__':
    a = SendEmail()
    a.sendMail()