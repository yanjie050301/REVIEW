"""
功能介绍：
        1.配置邮件属性
        2.组装邮件内容和标题
        3.发送邮件，内容包括正文和附件

"""
import smtplib
import time,os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logconfig import log
from readconfig import ConfigRead


class SendEmail():
    def __init__(self):
        c = ConfigRead()
        #1.配置邮件属性
        self.sender = c.reademail("sender")  # 发件人邮箱
        self.receiver = c.reademail("receiver")   # 接收人邮箱
        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())  # 发送邮件的时间
        self.titel = "自动化测试结果——" + t  # 拼接邮件的标题
        self.smtpserver = c.reademail("smtpserver")   # 发送邮箱的服务器
        self.username = c.reademail("username")   # 登录邮箱的用户名
        # 注意：如果邮箱从未开启过pop3/smtp服务，则需要进入邮箱设置开启，开启成功后会提示一个授权码，把此处的密码替换为生成的授权码即可
        self.password = c.reademail("password")  # 登录邮箱的授权码
    def email(self):
        #2.组装邮件内容和标题
        # 查找附件
        base_path = os.path.dirname(os.path.dirname(__file__))   #查找到apitext目录
        new_path = base_path + "\\Report"   #拼接到Report目录
        l = os.listdir(new_path)            #将Report目录所有文件取出来
        file = l[len(l) - 2]      #找最新的测试报告，因为生成的报告都是自动按照时间升序排序，所以直接取最后一个测试报告就可以
        new_file = new_path + "\\" +file     #拼接最新的测试报告路径
        with open(new_file, "rb") as f:
            # 添加附件
            mail_body = f.read()
            self.msg = MIMEMultipart("alternative")
            # **************第二步：组装邮件内容和标题，中文需要参数“utf-8”,单字节字符不需要加参数
            # 在邮件中加入文本内容
            content = "Python邮件发送测试..."
            msgtext = MIMEText(content, "plain", "utf-8")  # plain是字体，utf-8是编码方式
            # 将文本内容加载到msg中
            self.msg.attach(msgtext)
            att = MIMEText(mail_body, "plain", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename=report.html'
            # 将邮件加载到msg中
            self.msg.attach(att)
            self.msg["Subject"] = Header(self.titel, "utf-8")
            self.msg["From"] = self.sender
            self.msg["To"] = self.receiver
    def sendemail(self):
        # 3.发送邮件，内容包括正文和附件
        self.email()
        logger = log()
        try:
            # 实例化SMTP类
            s = smtplib.SMTP()
            # 连接smtp服务器
            s.connect(self.smtpserver)
            # 登录邮箱
            s.login(self.username, self.password)
            # 设置发件人，收件人和邮件内容
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
        except:
            logger.info("邮件发送失败")
        else:
            logger.info("邮件发送成功")
        finally:
            # 退出服务器
            s.quit()
if __name__ == '__main__':
    a = SendEmail()
    a.sendemail()













