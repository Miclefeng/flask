#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/15 0:24
#=============================================================
# coding:utf8
from app import mail
from flask_mail import Message


def send_mail():
    msg = Message('测试邮件', sender='1280054628@qq.com', body='Test', recipients=['miclefengzss@163.com'])
    mail.send(msg)