"""
功能说明
1.配置邮箱，将生成的测试报告发送到指定的邮箱
思路：
    1.配置邮件属性
    2.组装邮件内容和标题,包括邮件正文和附件
    3.附件筛选测试报告最新的HTML文件
    4.登录邮箱服务器，发送邮件
"""
import smtplib
import time,os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.readconfig import ConfigRead
class Emailcon():
    def __init__(self):
        c = ConfigRead()
        #1.配置邮件属性
        self.sender = c.reademail("sender")  #获取发件人邮箱
        self.receiver = c.reademail("receiver")   #获取收件人邮箱
        self.username = c.reademail("username")    #登录邮箱的用户名
        self.password = c.reademail("password")      #登录邮箱的密码
        self.smtpserver = c.reademail("smtpserver")   #发送邮箱的服务器
        t = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())   #邮箱发送时间
        self.title = "自动化测试报告--"+t  #邮件标题，与时间拼接
    def email(self):
        #2.组装邮件内容和标题,包括邮件正文和附件
        #查找附件
        path = os.path.dirname(os.path.dirname(__file__)) + "//TestReport"  #测试报告路径
        list_file = os.listdir(path)    #获取路径下所有文件
        report_file = list_file[0]    #获取最新的测试报告，由于每次生成测试报告之前都会把旧的报告删除，所以文件夹里面只有一个最新的测试报告
        report_parh = path + "//" + report_file   #拼接最新的测试报告路径
        with open(report_parh,"rb") as f:
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
            self.msg["Subject"] = Header(self.title, "utf-8")
            self.msg["From"] = self.sender
            self.msg["To"] = self.receiver
    def sendemail(self):
        # 3.发送邮件，内容包括正文和附件
        self.email()
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
            print("邮件发送失败")
        else:
            print("邮件发送成功")
        finally:
            # 退出服务器
            s.quit()


if __name__ == '__main__':
    a = Emailcon()
    a.sendemail()




























