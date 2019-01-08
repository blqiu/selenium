#coding:utf-8
import os
import unittest
from utils.mail import Email
from utils.config import Config
from utils import HTMLTestRunner
from utils import log

# 用例路径
case_path = os.path.join(os.getcwd(), ".")
report_file = Config.REPORT_FILE
def all_case():
    allcase = unittest.defaultTestLoader.discover(case_path, pattern="demo*.py", top_level_dir=None)
    return allcase

def send_mail():
    e = Config()
    sender = e.getInfo("mail", "sender")
    passwd = e.getInfo("mail", "passwd")
    receiver = e.getInfo("mail", "receiver")
    smtp_server = e.getInfo("mail", "smtp_server")
    Email.send_mail(sender, passwd, receiver, smtp_server, report_file)

if __name__ == "__main__":
    rf = open(report_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=rf,
        title=u'这是我的测试报告',
        description=u'用例执行情况.'
    )
    runner.run(all_case())
    rf.close()
    send_mail()