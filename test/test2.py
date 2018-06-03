#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/3 17:44
#=============================================================
# coding:utf8
import threading
import time


class A:
    b = 1

my_obj = A()

def worker():
    my_obj.b = 2

# 主线程
print(my_obj.b)

new_t = threading.Thread(target=worker, name='Miclefeng')
new_t.start()
time.sleep(1)

# 主线程
print(my_obj.b)