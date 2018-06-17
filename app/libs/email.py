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
from threading import Thread


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1280054628@qq.com', body='Test', recipients=['miclefengzss@163.com'])
    msg = Message('[鱼书]' + ' ' + subject, 
    	sender=current_app.config['MAIL_USERNAME'],
    	recipients=[to])
    msg.html = render_template(template, **kwargs)
    # current_app 代理对象通过线程的ID去找flask核心对象,本身就做了线程隔离
    # 获取flask的核心对象
    app = current_app._get_current_object()
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()

def send_async_email(app, msg):
	with app.app_context():
		try:
			mail.send(msg)
		except Exception as e:
			pass
