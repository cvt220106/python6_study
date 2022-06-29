# @Author : 杨佳杰
# @Time   : 2022/6/20 13:58
# @File   : 4-多线程共享全局变量-不加锁.py
# @Author : 杨佳杰
# @Time   : 2022/6/20 10:47
# @File   : 5-多线程共享全局变量.py
import threading
import time

g_num = 0


def work1():
    global g_num
    for i in range(100000000):
        g_num += 1


def work2():
    global g_num
    for i in range(100000000):
        g_num += 1


if __name__ == '__main__':
    start_time = time.time()
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'线程执行结束后g_num={g_num}')
    end_time = time.time()
    print(f'程序执行耗时{end_time - start_time:.3f}s')
