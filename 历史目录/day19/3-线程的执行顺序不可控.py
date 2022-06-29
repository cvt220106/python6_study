# @Author : 杨佳杰
# @Time   : 2022/6/20 13:55
# @File   : 3-线程的执行顺序不可控.py
# @Author : 杨佳杰
# @Time   : 2022/6/20 13:48
# @File   : 2-面向对象创建进程.py
import threading
import time


class MyThread(threading.Thread):
    # 重点在于重写run方法来执行线程代码
    def run(self):
        for i in range(5):
            time.sleep(1)
            print(f'I am {self.name} @: {i}')
            # name属性为线程对应的线程名


def main():
    for i in range(4):
        t = MyThread()
        t.start()  # 线程的start方法中调用了我们重写run方法


if __name__ == '__main__':
    main()
