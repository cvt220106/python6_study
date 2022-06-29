# @Author : 杨佳杰
# @Time   : 2022/6/29 19:33
# @File   : 6-类装饰器.py
"""
装饰器函数其实是这样一个接口约束，它必须接受一个 callable 对象作为参数,然后返回一个 callable对象。
在 Python 中一般 callable对象都是函数，但也有例外。
只要某个对象重写了__call__()方法，那么这个对象就是 callable 的。
"""

class Test:
    def __init__(self,func):
        print('--初始化--')
        print(f'func name is {func.__name__}')
        self.__func=func
        # 将被装饰的函数作为一个属性传入，并设置为一个私密属性，来由对象内部的__call__方法使用，从而引用对应函数

    def __call__(self, *args, **kwargs):
        print('--装饰器效果--')
        self.__func() # 相当于装饰器闭包函数中的func()

@Test # 相当于执行了test=Test(test)
def test():
    print('--test--')
test()
