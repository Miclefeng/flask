###############################################################
# File Name: app.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 23 May 2018 09:44:10 PM CST
#=============================================================
# coding:utf8
#from flask import Flask, make_response

#app = Flask(__name__)
# 导入模块的路径
#app.config.from_object('config')
# 导入模块中的代码必须为大写
# print(app.config['DEBUG'])

#@app.route("/hello")
#def hello():
    # 视图函数 返回 status_code 200, content-typ http headers
    # content-type = text/html default
    # Response 对象
    #headers = {
    #            'content-type' : 'text/html'
    #        }
    # response = make_response('<html></html>', 200)
    # response.headers = headers
    # return response
    #return '<html></html>', 200, headers # 其实是一个元组
# 路由注册方式，param url地址，view_func视图函数
# app.add_url_rule('/hello', view_func=hello)

# <q> <page> request_uri
#@app.route("/book/search/<q>/<page>")
#def search(q, page):
#    """
#    q : isbn or key
#    page
#    """
#    isbn_or_kw = is_isbn_or_kw(q)
#    if 'isbn' == is_isbn_or_kw:
#        res = FisherBook.search_by_isbn(q)
#    else:
#        res = FisherBook.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type' : 'application/json'}
#    return jsonify(res)
from app import create_app

app = create_app()

# if __name__ 只在自己模块中才能运行
if __name__ == '__main__':
    # host 指定host地址
    # 生产环境 nginx+uwsgi 作为服务器,与app.run()服务器产生冲突
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8002)
