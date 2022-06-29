# @Author : 杨佳杰
# @Time   : 2022/6/19 0:10
# @File   : work4-进程池创建.py
from multiprocessing import Manager, Pool
import time, os


def read_proc(q):
    print(f'父进程{os.getppid()}的读子进程{os.getpid()}启动!')
    for i in range(q.qsize()):
        read=q.get()
        print(f'读子进程从消息队列中读取{read}')


def write_proc(q):
    print(f'父进程{os.getppid()}的写子进程{os.getpid()}启动!')
    for i in 'hellopython':
        print(f'写子进程从消息队列中写入{i}')
        q.put(i)
    time.sleep(3)


if __name__=='__main__':
    print(f'父进程{os.getpid()}启动!')
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()  # 如果进程池中不设置进程数，每次派一个任务，就会启动一个进程
    po.apply_async(write_proc, (q,))

    time.sleep(1)  # 先让上面的任务向Queue存入数据，然后再让下面的任务开始从中取数据

    po.apply_async(read_proc, (q,))
    po.close()
    po.join()
    print(f'父进程{os.getpid()}执行结束!')


