#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/5/26 15:31
#=============================================================
# coding:utf8
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class SearchForm(Form):
    # q为文本类型
    q = StringField(DataRequired(), validators=[length(min=1, max=30, message='参数错误')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)