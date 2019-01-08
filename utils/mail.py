# coding:utf-8
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import report
class Email:
    def send_mail(sender, passwd, receiver, smtpserver, report_file):
        f1 = open(report_file, "rb")
        msg = MIMEMultipart()
        body = MIMEText(f1.read(), _subtype='html', _charset='utf-8')
        f1.close()
        msg['Subject'] = u"自动化测试报告"
        msg["from"] = sender
        msg["to"] = ";".join(receiver)
        msg.attach(body)
        # 添加附件
        f2 = open(report_file, "rb")
        att = MIMEText(f2.read(), "base64", "utf-8")
        f2.close()
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "result.html"'
        msg.attach(att)
        # 登录邮箱
        smtp = smtplib.SMTP()
        # 连接邮箱服务器
        smtp.connect(smtpserver)
        # 用户名密码
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('email has send out !')
