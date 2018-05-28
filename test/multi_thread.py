#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/5/28 23:54
#=============================================================
# coding:utf8
import threading
import time


def worker():
    time.sleep(1)
    print('I am thread')
    t = threading.current_thread()
    print(t.getName())

new_t = threading.Thread(target=worker, name='Miclefeng')
new_t.start()

# python 不能充分利用多核CPU优势
# GIL 全局解释器锁 global interpreter lock
t = threading.current_thread()
print(t.getName())

