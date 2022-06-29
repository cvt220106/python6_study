# @Author : 杨佳杰
# @Time   : 2022/6/18 23:52
# @File   : work3-两个读写子进程之间通信.py
from multiprocessing import Process, Queue
import time


def write_proc(q: Queue):
    for value in ['A', 'B', 'C']:
        print(f'向消息队列写入{value}')
        q.put(value)
        time.sleep(1)


def read_proc(q: Queue):
    while True:
        if not q.empty():  # 当消息队列不为空时才读取消息
            value = q.get()  # 读取一条消息
            print(f'从消息队列中读取到{value}')
            time.sleep(1.5)  # 通过sleep来实现,写入一条,读一条的效果
        else:  # 消息队列为空,则不再读取,退出循环
            break


if __name__ == '__main__':
    q = Queue()  # 创建消息队列
    # 创建读写子进程
    pw = Process(target=write_proc, args=(q,))
    pr = Process(target=read_proc, args=(q,))
    pw.start()  # 先启动写进程,让消息队列中存在消息,再让读进程读取消息
    time.sleep(0.5)  # 确保读进程先处理
    pr.start()
    pw.join()
    pr.join()
