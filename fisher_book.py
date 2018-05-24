###############################################################
# File Name: fisher_book.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 10:33:41 PM CST
#=============================================================
# coding:utf8
from http import HTTP

class FisherBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        res = HTTP.get(url)
        return res
