#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/17 11:03
#=============================================================
# coding:utf8
from enum import Enum


class PendingStatus(Enum):
    '''交易的4中状态'''
    Waitind = 1
    Success = 2
    Reject = 3
    Redraw = 4