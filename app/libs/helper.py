###############################################################
# File Name: helper.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 12:44:52 AM CST
#=============================================================
# coding:utf8

def is_isbn_or_kw(word):
# isbn13 13个数字组成
# isbn10 10个数字组成，可能含有
    isbn_or_kw = 'kw' # isbn or 关键字
    if 13 == len(word) and word.isdigit():
        isbn_or_kw = 'isbn'
    else:
        short_word = word.replace('-', '')
        if '-' in word and 10 == len(short_word) and short_word.isdigit():
            isbn_or_kw = 'isbn'
    return isbn_or_kw
