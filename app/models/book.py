#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/5/26 21:00
#=============================================================
# coding:utf8

# sqlalchemy
# Flask_SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    author = Column(String(31), default='佚名')
    binding = Column(String(16))
    publisher = Column(String(64))
    price = Column(String(24))
    pages = Column(Integer)
    pubdate = Column(String(24))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(512))
    image = Column(String(64))