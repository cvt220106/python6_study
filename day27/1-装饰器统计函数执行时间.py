# @Author : 杨佳杰
# @Time   : 2022/6/29 11:22
# @File   : 1-装饰器统计函数执行时间.py
import time

def cal_excute_time(func):
    def call_func():
        start=time.time()
        func()
        end=time.time()
        print(f'use time={end-start}s')
    return call_func

@cal_excute_time
def test():
    print('--test--')
    for i in range(100000):
        pass

test()