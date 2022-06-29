# @Author : 杨佳杰
# @Time   : 2022/6/29 17:34
# @File   : 2-有参数函数的装饰器练习.py
import time

def test_func(func):
    def call_func(a,b):
        """
        有参数函数的使用装饰器时，装饰器内的闭包函数也一定要有对应的参数
        并且要将参数传入最后装饰器要调用的函数
        :param a:
        :param b:
        :return:
        """
        print(f'{func.__name__} called at {time.ctime()}')
        func(a,b)
    return call_func

@test_func
def test(a,b):
    print(a+b)

test(1,2)
time.sleep(2)
test(2,3)