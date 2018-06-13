#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/7 23:07
#=============================================================
# coding:utf8
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, desc, func
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.wish import Wish
from flask import current_app
from app.spider.fisher_book import FisherBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id')
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        fisher_book = FisherBook()
        fisher_book.search_by_isbn(self.isbn)
        return fisher_book.first

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False, status=1).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(Wish.isbn).all()
        return [{'count' : w[0], 'isbn': w[1]} for w in count_list]

    # 对象代表一个礼物，具体的事物
    # 类代表这个事物，是抽象的，不是具体的“一个”
    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
