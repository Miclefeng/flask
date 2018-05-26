###############################################################
# File Name: __init__.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 25 May 2018 12:01:19 AM CST
#=============================================================
# coding:utf8
from flask import Blueprint

# 蓝图 blueprint
web = Blueprint('web', __package__)

from app.web import book
from app.web import user
