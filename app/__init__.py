###############################################################
# File Name: __init__.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 11:57:20 PM CST
#=============================================================
# coding:utf8

from flask import Flask


def init_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app

def register_blueprint(applaction):
    from app.web.book import web
    applaction.register_blueprint(web)
