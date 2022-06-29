# @Author : 杨佳杰
# @Time   : 2022/6/19 1:31
# @File   : work6-多线程while查看cpu.py
from threading import Thread


def while1():
    while True:
        pass


if __name__ == '__main__':
    t = Thread(target=while1)
    t.start()
    while True:
        pass
