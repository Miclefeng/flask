#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/3 23:16
#=============================================================
# coding:utf8


class BookViewModel:
    def __init__(self, fisher_book):
        self.title = fisher_book['title']
        self.publisher = fisher_book['publisher']
        self.pages = fisher_book['pages']
        self.author = fisher_book['author']
        self.price = fisher_book['price']
        self.summary = fisher_book['summary']
        self.image = fisher_book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, fisher_book, keyword):
        self.total = fisher_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in fisher_book.books]


class _BookViewModel:

    @classmethod
    def pack_single(cls, data, keyword):
        res = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            res['total'] = 1
            res['data'] = cls.__cut_book_data(data)
        return res

    @classmethod
    def pack_collection(cls, data, keyword):
        res = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            res['total'] = data['total']
            res['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return res

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': data['author'],
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'],
        }
        return book
