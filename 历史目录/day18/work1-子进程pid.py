# @Author : 杨佳杰
# @Time   : 2022/6/18 23:08
# @File   : work1-子进程pid.py
from multiprocessing import Process
import os


def test_proc():
    """子进程"""
    print(f'子进程的pid为{os.getpid()}')
    print('子进程运行结束!')

"""
若父进程执行结束,但子进程未结束时,Python中父进程会等待子进程结束
回收子进程资源后,父进程才结束!
"""


if __name__ == '__main__':
    print(f'父进程的pid为{os.getpid()}')
    p = Process(target=test_proc)  # 创建子进程!
    p.start()  # 启动子进程!
