###############################################################
# File Name: __init__.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 25 May 2018 12:01:19 AM CST
#=============================================================
# coding:utf8
from flask import Blueprint, render_template

# 蓝图 blueprint
web = Blueprint('web', __package__, template_folder='../templates')

@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import user
