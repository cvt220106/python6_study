# @Author : 杨佳杰
# @Time   : 2022/6/20 10:09
# @File   : 1-主线程默认等待子线程.py
import threading
import time


def sing():
    for i in range(5):
        print(f'正在唱歌...{i}')
        time.sleep(1)


def dance():
    for i in range(5):
        print(f'正在跳舞...{i}')
        time.sleep(1)


if __name__ == '__main__':
    print(f'开始-----{time.ctime()}')
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print(f'当前进程数:{len(threading.enumerate())}')
    t1.join()
    t2.join()
    print(f'当前进程数:{len(threading.enumerate())}')
    print(f'结束-----{time.ctime()}')
