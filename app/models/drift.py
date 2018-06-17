#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/17 10:44
#=============================================================
# coding:utf8
from app.libs.enums import PendingStatus
from app.models.base import Base
from sqlalchemy import Column, Integer, String, SmallInteger


class Drift(Base):
    '''
    一次交易具体的信息
    '''
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(24), nullable=False)
    address = Column(String(128), nullable=False)
    message = Column(String(256))
    mobile = Column(String(16), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(64))
    book_author = Column(String(32))
    book_img = Column(String(128))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(24))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(24))

    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value

