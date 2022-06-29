# @Author : 杨佳杰
# @Time   : 2022/6/28 22:13
# @File   : work4-多个装饰器执行顺序.py
def add_first(func):
    print('--开始装饰---1')# 2
    def call_func(*args,**kwargs):
        print('--开始验证权限--1')# 3
        func(*args,**kwargs)
    return call_func


def add_second(func):
    print('--开始装饰---2')# 1
    def call_func(*args,**kwargs):
        print('--开始验证权限--2')# 4
        func(*args,**kwargs)
    return call_func

@add_first
@add_second
def test():
    print('--test--')


test()


def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test1():
    return 'hello-world'


print(test1())