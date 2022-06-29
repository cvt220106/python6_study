# @Author : 杨佳杰
# @Time   : 2022/6/29 19:15
# @File   : 5-在装饰时加入参数.py
import time
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrapped_func():
            print(f"{func.__name__} called at {time.ctime()} {pre}" )
            return func()
        return wrapped_func
    return timefun
# 下面的装饰过程
# 1. 调用 timefun_arg()
# 2. 将步骤 1 得到的返回值，即 time_fun 返回， 然后 time_fun(foo)
# 3. 将 time_fun(foo)的结果返回，即 wrapped_func
# 4. 让 foo = wrapped_fun，即 foo 现在指向 wrapped_func
@timefun_arg()# 默认参数hello
def test():
    print('i am test')

test()
time.sleep(1)
@timefun_arg('wolrd')
def test():
    print('i am test')

test()
time.sleep(1)
@timefun_arg('python')  # 默认参数hello
def test():
    print('i am test')

test()