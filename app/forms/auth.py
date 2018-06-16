#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/8 0:36
#=============================================================
# coding:utf8
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from app.models.user import User


class EmailForm(Form):
    email = StringField(validators=[DataRequired(message='邮箱不能为空'), Length(8, 64), Email(message='电子邮箱不符合规范')])

class LoginForm(EmailForm):
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 24)])


class RegisterForm(LoginForm):
    nickname = StringField(validators=[DataRequired(), Length(2, 12, message='昵称至少为2个字符，至多12个字符')])

    def validate_email(self, field):
        # db.session.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_nickname(self, field):
        # db.session.
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('用户昵称已被注册')


class ResetPasswordForm(Form):
    passwd1 = PasswordField(validators=[DataRequired(), Length(6, 24, message='密码需要在6到32个字符之间'), EqualTo('passwd2', message='两次输入的密码不相同')])

    passwd2 = PasswordField(validators=[DataRequired(), Length(6, 24)])
