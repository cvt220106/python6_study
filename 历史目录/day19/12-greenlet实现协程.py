# @Author : 杨佳杰
# @Time   : 2022/6/20 15:25
# @File   : 12-greenlet实现协程.py
from greenlet import greenlet
import time


def test1():
    while True:
        print('--a--')
        gr2.switch()  # 只能主动切换
        time.sleep(0.5)


def test2():
    while True:
        print('--b--')
        gr1.switch()  # 只能主动切换
        time.sleep(0.5)


# 创建协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)
# 切换到gr1开始运行
gr1.switch()
