# @Author : 杨佳杰
# @Time   : 2022/6/20 15:42
# @File   : 13-gevent实现自动切换协程.py
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 模拟一个sleep操作，使得各协程之间发生切换
        gevent.sleep(1)


# 接口使用方法gevent.spawn(函数名,传参)
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
