# 在Python发送邮件
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'yamon1437@163.com'
    rreceiver = '1165828007@qq.com'
    message = MIMEText('用python发送邮件实例代码', 'plain', 'utf-8')
    message['From'] = Header('陈亚萌', 'utf-8')
    message['To'] = Header('yamon', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(sender, 'cym1437qi')
    smtper.sendmail(sender, rreceiver, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()