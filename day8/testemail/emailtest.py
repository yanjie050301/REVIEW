"""
功能描述：
1.配置邮箱属性
2.组装邮件内容和标题，中文需要参数“utf-8”,单字节字符不需要加参数
"""

#发送HTML内容的邮件
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header


def sendMail():
    """
# 发送内容邮件
"""
    #***************第一步：配置邮箱属性
    sender = "18911032248@163.com"   #发件人邮箱
    receiver = "1353037583@qq.com"   #接收人邮箱
    t = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())   #发送邮件的时间
    # print(t)
    titel = "自动化测试结果——" + t    #拼接邮件的标题
    smtpserver = "smtp.163.com"    #发送邮箱的服务器
    username = "18911032248@163.com"  #登录邮箱的用户名
    # 注意：如果邮箱从未开启过pop3/smtp服务，则需要进入邮箱设置开启，开启成功后会提示一个授权码，把此处的密码替换为生成的授权码即可
    password = "IXFQVCYWTXMHQXFO"         #登录邮箱的授权码
    content = "Python邮件发送测试..."
    #**************第二步：组装邮件内容和标题，中文需要参数“utf-8”,单字节字符不需要加参数
    msg = MIMEText(content,"plain","utf-8")
    # print(msg)
    msg["Subject"] = Header(titel,"utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    #*************第三步：登录并发送邮件
    try:
        #实例化SMTP类
        s = smtplib.SMTP()
        #连接smtp服务器
        s.connect(smtpserver)
        #登录邮箱
        s.login(username,password)
        #设置发件人，收件人和邮件内容
        s.sendmail(sender,receiver,msg.as_string())
    except:
        print("邮件发送失败")
    else:
        print("邮件发送成功")
    finally:
        #退出服务器
        s.quit()

sendMail()
