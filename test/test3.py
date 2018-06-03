#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/6/3 17:49
#=============================================================
# coding:utf8
import threading
import time
from werkzeug.local import Local

# 实现线程隔离原理，使用字典保存数据
# werkzeug local Local
# Local 使用字典的方式实现的线程隔离
# LocalStack 是线程隔离的栈结构
# 使用线程隔离的意义在于： 是当前线程能够正确的引用到它自己所创建的对象，而不是引用到其他线程所创建的对象
class A:
    b = 1

my_obj = Local()
my_obj.b = 1

def worker():
    # 新线程
    my_obj.b = 2
    print('In new thread b is: ' + str(my_obj.b))

new_t = threading.Thread(target=worker, name='Miclefeng')
new_t.start()
time.sleep(1)

# 主线程
print('In main thread b is: ' + str(my_obj.b))