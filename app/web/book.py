###############################################################
# File Name: book.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 11:25:30 PM CST
#=============================================================
# coding:utf8

from flask import jsonify, request
from app.forms.book import SearchForm
from helper import is_isbn_or_kw
from fisher_book import FisherBook
from . import web


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q : keyword or isbn
        page
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        pqge = form.page.data
        isbn_or_key = is_isbn_or_kw(q)
        if 'isbn' == isbn_or_key:
            res = FisherBook.search_by_isbn(q)
        else:
            res = FisherBook.search_by_keyword(q, page)
        return jsonify(res)
        # return json.dumps(result), 200, {'content-type' : 'application/json'}
    else:
        return jsonify(form.errors)

@web.route('/book/find')
def find():
    # flask request response
    # request 必须在falsk的上下文环境中，http请求、视图函数中
    # q = request.args['q']
    # p = request.args.to_dict()
    # page = request.args['page']
    # 参数校验，验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_kw(q)
        if 'isbn' == isbn_or_key:
            res = FisherBook.search_by_isbn(q)
        else:
            res = FisherBook.search_by_keyword(q)
        return jsonify(res)
    else:
        return jsonify(form.errors)

