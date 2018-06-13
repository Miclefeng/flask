#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/13 1:01
#=============================================================
# coding:utf8
from .book import BookViewModel
from collections import namedtuple

MyWish = namedtuple('MyWish', ['id', 'book', 'wishes_count'])

class MyWishes:
    def __init__(self, wishes_of_mine, gift_count_list):
        self.__wishes_of_mine = wishes_of_mine
        self.__gift_count_list = gift_count_list
        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            temp_wishes.append(self.__matching(wish))
        return temp_wishes

    def __matching(self, wish):
        count = 0
        for gift_count in self.__gift_count_list:
            if gift_count['isbn'] == wish.isbn:
                count = gift_count['count']
                break

        r = {
            'id': wish.id,
            'book': BookViewModel(wish.book),
            'wishes_count': count
        }
        return r