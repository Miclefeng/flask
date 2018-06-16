# =============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/7 23:07
# =============================================================
# coding:utf8
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from app.libs.helper import is_isbn_or_kw
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.fisher_book import FisherBook
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class User(UserMixin, Base):
    # 设置表名
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    _password = Column('password', String(128))
    wx_open_id = Column(String(48))
    wx_name = Column(String(32))
    # gifts = relationship('Gift')

    # 数据的预处理 getter setter
    # 属性的读取
    @property
    def password(self):
        return self._password

    # 属性的写入
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_kw(isbn) != 'isbn':
            return False

        fisher_book = FisherBook()
        fisher_book.search_by_isbn(isbn)
        if not fisher_book.first:
            return False

        # 不允许用户同时赠送多本相同的图书
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        # 一个用户不能同时为赠送者和索要者
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        # 既不在赠送清单，也不在心愿清单
        if not gifting and not wishing:
            return True
        else:
            return False

    def generate_token(self, expire=600):
        s = Serializer(current_app.config['SECRET_KEY'], expire)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except Exception as e:
            return False
        uid = data.get('id')
        print('\n\n\n')
        print(uid)
        with db.auto_commit():
            user = User.query.get(uid)
            print(user)
            print('\n\n\n')
            user.password = new_password
        return True


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
