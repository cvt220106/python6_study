# 作者: 王道 龙哥
# 2022年06月18日10时08分48秒
# 作者: 王道 龙哥
# 2022年06月18日09时54分55秒
from multiprocessing import Process
import os
import time

def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')
    while True:
        time.sleep(1)

if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
    p.terminate()#主动终止子进程后,父进程仍在运行,此时子进程占有资源,为僵尸进程状态!
    time.sleep(10)
    p.join()#主动join()子进程的占有资源,子进程脱离僵尸状态,子进程消失!
    time.sleep(10)