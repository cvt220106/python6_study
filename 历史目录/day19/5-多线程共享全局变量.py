# @Author : 杨佳杰
# @Time   : 2022/6/20 10:47
# @File   : 5-多线程共享全局变量.py
import threading
import time

g_num = 0


def work1(mutex):
    global g_num
    print(id(mutex))
    for i in range(100000000):
        # 执行加法操作访问g_num时加锁,
        mutex.acquire()
        g_num += 1
        mutex.release()


def work2(mutex):
    print(id(mutex))
    global g_num
    for i in range(100000000):
        mutex.acquire()
        g_num += 1
        mutex.release()


def main():
    mutex = threading.Lock()
    print(id(mutex))
    # 创建一个互斥锁,在main中创建时,属于全局变量,无需传入,但在函数方法中创建时,则需传入给线程
    t1 = threading.Thread(target=work1, args=(mutex,))
    t1.start()
    t2 = threading.Thread(target=work2, args=(mutex,))
    t2.start()
    t1.join()
    t2.join()
    print(f'线程执行结束后g_num={g_num}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'程序执行耗时{end_time - start_time:.3f}s')
    # 加锁后,一个线程执行时,另外一个线程会进入等待阻塞态,这也导致了运行时间变长
    # 不加锁:1.550s,加锁后:8.991s
