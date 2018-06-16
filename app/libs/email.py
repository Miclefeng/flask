#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/15 0:24
#=============================================================
# coding:utf8
from app import mail
from flask_mail import Message
from flask import current_app, render_template


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1280054628@qq.com', body='Test', recipients=['miclefengzss@163.com'])
    msg = Message('[鱼书]' + ' ' + subject, 
    	sender=current_app.config['MAIL_USERNAME'],
    	recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)