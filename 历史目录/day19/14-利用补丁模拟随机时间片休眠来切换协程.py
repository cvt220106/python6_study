# @Author : 杨佳杰
# @Time   : 2022/6/20 15:50
# @File   : 14-利用补丁模拟随机时间片休眠来切换协程.py
from gevent import monkey
import gevent
import random
import time

# 将程序中用到的耗时操作代码转换为gevent内部自己实现的模块
monkey.patch_all()


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(coroutine_work, 'work1'),
    gevent.spawn(coroutine_work, 'work2')
])
