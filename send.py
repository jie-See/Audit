# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText


def send_mail(sub, content):
    mailto_list = ['Jie__See@163.com']  # 收件人(列表)
    mail_host = "smtp.qq.com"  # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
    mail_user = "739698292@qq.com"  # 用户名
    mail_pass = "eavtszgekaptbcdc"  # 密码  网易邮箱需要使用授权码
    mail_postfix = "163.com"  # 邮箱的后缀，网易就是163.com
    me = "739698292@qq.com"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)  # 将收件人列表以‘；’分隔
    # try:
    server = smtplib.SMTP(mail_host)
    server.connect(mail_host)  # 连接服务器
    server.login(mail_user, mail_pass)  # 登录操作
    server.sendmail(me, mailto_list, msg.as_string())
    server.close()
    return True
    # except(Exception):
        # print( str(e) )
    return False


# for i in range(1):  # 发送1封，上面的列表是几个人，这个就填几
#     if send_mail("你好", "卡贷款oandgoj%&&*^*&^*&%%jkdjnfidn"):  # 邮件主题和邮件内容
#         # 这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
#         print("done!")
#     else:
#         print("failed!")
