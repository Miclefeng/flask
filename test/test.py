#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/5/27 11:28
#=============================================================
# coding:utf8
from flask import Flask, current_app, request, Request

app = Flask(__name__)

# 应用上下文 对象 对Flask的封装
# 请求上下文 对象 对Request的封装
# Flask AppContext
# Request RequestContext

# 离线应用、单元测试 需要手动推入app_stack
# app_ctx = app.app_context()
# app_ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# app_ctx.pop()

# 实现了上下文协议的对象使用with
# 上下文管理器 即实现了 __enter__ __exit__
# 上下文表达式必须返回一个上下文管理器
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']


class A:

    # 返回class本身，供 as 使用
    def __enter__(self):
        print('connect to resource')
        return self

    # 返回 True or FALSE
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')

        print('close resource connection')
        # 返回 True 外部不会捕捉到异常, False 可以捕获
        return False

    def query(self):
        print('query data')

# obj_a 时 __enter__ 返回的值
try:
    # resource 为 __enter__ 方法返回的变量
    with A() as resource:
        # 1/0
        resource.query()
except:
    pass