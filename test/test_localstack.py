#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/3 18:27
#=============================================================
# coding:utf8
import threading
import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)
print('In main thread after push, value is: ' + str(my_stack.top))

def worker():
    # 新线程
    print('In new thread before push, value is: ' + str(my_stack.top))
    my_stack.push(2)
    print('In new thread after push, value is: ' + str(my_stack.top))

new_t = threading.Thread(target=worker, name='Micle')
new_t.start()
time.sleep(1)

# 主线程
print('finally, In main thread value is: ' + str(my_stack.top))