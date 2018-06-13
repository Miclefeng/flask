#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/7 23:07
#=============================================================
# coding:utf8
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, desc, func
from sqlalchemy.orm import relationship
from app.spider.fisher_book import FisherBook
from app.models.base import Base, db
from app.models.gift import Gift


class Wish(Base):
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
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(launched=False, uid=uid, status=1).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(Gift.isbn).all()
        return [{'count': g[0], 'isbn': g[1]} for g in count_list]
