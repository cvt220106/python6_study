# @Author : 杨佳杰
# @Time   : 2022/6/29 19:43
# @File   : 7-使用wraps确保被装饰函数的函数名和注释不变.py
from functools import wraps


def my_decorator(func):
    def wper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)  # wper decorator


def my_decorator(func):
    @wraps(func)  # warps的作用是让函数显示自己的名字和备注
    def wper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)  # wper decorator
