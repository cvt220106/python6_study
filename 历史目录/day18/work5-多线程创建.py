# @Author : 杨佳杰
# @Time   : 2022/6/19 1:27
# @File   : work5-多线程创建.py
import time
from threading import Thread

def print_hello():
    print('I say: hello!')
    time.sleep(1)


if __name__=='__main__':
    for i in range(5):
        t=Thread(target=print_hello)
        t.start()