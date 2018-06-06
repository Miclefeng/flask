###############################################################
# File Name: book.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 11:25:30 PM CST
#=============================================================
# coding:utf8
import json
from flask import jsonify, request, render_template, flash
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_kw
from app.spider.fisher_book import FisherBook
from app.view_models.book import BookCollection
from . import web


@web.route('/test1')
def test1():
    from app.libs.none_local import n
    from flask import request
    print(n.v)
    n.v = 2
    print('-------------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    return ''

@web.route('/book/search')
def search():
    """
        q : keyword or isbn
        page
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_kw(q)
        fisher_book = FisherBook()

        if 'isbn' == isbn_or_key:
            fisher_book.search_by_isbn(q)
        else:
            fisher_book.search_by_keyword(q, page)

        books.fill(fisher_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        return jsonify(form.errors)
    return render_template('search_result.html', books=books)

@web.route('/test')
def test():
    r = {
        'name': 'Miclefeng',
        'age': 26
    }
    flash('hello,miclefengzss', category='error')
    # 模板html
    return render_template('test.html', data=r)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass

