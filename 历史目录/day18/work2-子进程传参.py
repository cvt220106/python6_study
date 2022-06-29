# @Author : 杨佳杰
# @Time   : 2022/6/18 23:25
# @File   : work2-子进程传参.py
from multiprocessing import Process
import os
import time

nums = [11, 22]


def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))


def work2():
    """子进程要执行的代码"""
    print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))


def test_proc(name, age, *args, **kwargs):
    for i in range(5):
        print(f'子进程中,name:{name},age:{age},列表信息{args[0]}')
        print(kwargs)
    # 修改传参中列表值
    args[0][1] = 100
    print('子进程中修改后列表元素为', args[0])


if __name__ == '__main__':
    """
    lst=[1,2,3]
    p=Process(target=test_proc,args=('yang',21,lst),kwargs={'test':100})
    p.start()
    time.sleep(10)
    print('子进程修改后父进程的列表元素为',lst)
    #子进程中修改了列表元素,父进程中并不会发生改变
    """
    # 创建子进程，是自己的分身，子进程创建后全局变量的改变不会父亲
    p1 = Process(target=work1)
    p1.start()
    p1.join()
    print(nums)
    p2 = Process(target=work2)
    p2.start()
