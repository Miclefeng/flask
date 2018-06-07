#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/7 23:07
#=============================================================
# coding:utf8
from sqlalchemy.orm import relationship
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    # gifts = relationship('Gift')