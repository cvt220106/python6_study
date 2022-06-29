# @Author : 杨佳杰
# @Time   : 2022/6/17 20:46
# @File   : 4-父子进程.py
import time
from multiprocessing import Process


def process_test():
    while True:
        print('---2---')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=process_test)  # 此处传参类似于当初排序算法处的sort_method,不传()!
    p.start()
    while True:
        print('---1---')
        time.sleep(1)
