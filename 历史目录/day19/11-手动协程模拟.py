# @Author : 杨佳杰
# @Time   : 2022/6/20 15:17
# @File   : 11-手动协程模拟.py
#利用yield来实现
import time


def work1():
    while True:
        print('--1--')
        yield
        time.sleep(0.5)


def work2():
    while True:
        print('--2--')
        yield
        time.sleep(0.5)


def main():
    w1=work1()#生成器1
    w2=work2()#生成器2
    while True:#按顺序next唤醒,交替执行
        next(w1)
        next(w2)

if __name__ == '__main__':
    main()