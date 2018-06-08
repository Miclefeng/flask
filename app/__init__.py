###############################################################
# File Name: __init__.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 11:57:20 PM CST
#=============================================================
# coding:utf8

from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()

def init_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    login_manager.init_app(app)
    # 把 DB 注册到APP上
    db.init_app(app)
    db.create_all(app=app)
    with app.app_context():
       db.create_all()
    return app

def register_blueprint(applaction):
    from app.web.book import web
    applaction.register_blueprint(web)
