# @Author : 杨佳杰
# @Time   : 2022/6/29 18:45
# @File   : 4-装饰器中闭包函数与return.py
import time
def test_func(func):
    def call_func():
        print(f'{func.__name__} called at {time.ctime()}')
        return func()
    return call_func

@test_func
def test():
    # return '--test--'
    print('--test--')

ret=test()
print(ret)