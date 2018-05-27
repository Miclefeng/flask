###############################################################
# File Name: fisher_book.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 10:33:41 PM CST
#=============================================================
# coding:utf8
from flask import current_app
from app.libs.httper import HTTP


class FisherBook:
    pagesize = 15
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PAGESIZE'], cls.calculate_start(page))
        res = HTTP.get(url)
        return res

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PAGESIZE']
