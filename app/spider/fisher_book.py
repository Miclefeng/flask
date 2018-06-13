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
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        res = HTTP.get(url)
        self.__fill_single(res)

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PAGESIZE'], cls.calculate_start(page))
        res = HTTP.get(url)
        cls.__fill_collection(res)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PAGESIZE']

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']


