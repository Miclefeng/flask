#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/8 0:36
#=============================================================
# coding:utf8
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 24)])

    nickname = StringField(validators=[DataRequired(), Length(2, 12, message='昵称至少为2个字符，至多12个字符')])