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
        pass
