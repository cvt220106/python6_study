# @Author : 杨佳杰
# @Time   : 2022/6/20 16:18
# @File   : 15-并发下载器.py
import requests
from gevent import monkey
import gevent
import random
import time

# 将程序中用到的耗时操作代码转换为gevent内部自己实现的模块
# monkey.patch_all()


def coroutine_work(url):
    print('GET: %s' % url)
    response = requests.get(url)
    data = response.text
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(coroutine_work, 'http://www.cskaoyan.com/'),
    gevent.spawn(coroutine_work, "http://www.cskaoyan.com/"),
    gevent.spawn(coroutine_work, "http://www.qq.com/")
])
