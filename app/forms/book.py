#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/5/26 15:31
#=============================================================
# coding:utf8
from wtforms import Form, StringField, IntegerField
from wtforms.validators import NumberRange, DataRequired, Length, Regexp


class SearchForm(Form):
    # q为文本类型
    q = StringField(DataRequired(), validators=[Length(min=1, max=30, message='参数错误')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField(validators=[DataRequired(), Length(min=2, max=20, message='收件人姓名长度必须在2到20个字符之间')])
    mobile = StringField(validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField()
    address = StringField(validators=[DataRequired(), Length(min=10, max=70, message='地址还不到10个字，请尽量写详细一些吧')])