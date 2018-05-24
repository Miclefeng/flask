###############################################################
# File Name: book.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 11:25:30 PM CST
#=============================================================
# coding:utf8

from flask import jsonify
from flask import Blueprint
from helper import is_isbn_or_kw
from fisher_book import FisherBook

# 蓝图 blueprint
web = Blueprint('web', __name__)

@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q : keyword or isbn
        page
    """
    isbn_or_key = is_isbn_or_kw(q)
    if 'isbn' == isbn_or_key:
        res = FisherBook.search_by_isbn(q)
    else:
        res = FisherBook.search_by_keyword(q)
    return jsonify(res)
    # return json.dumps(result), 200, {'content-type' : 'application/json'}
