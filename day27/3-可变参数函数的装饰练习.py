# @Author : 杨佳杰
# @Time   : 2022/6/29 18:31
# @File   : 3-可变参数函数的装饰练习.py
def test_func(func):
    def call_func(*args,**kwargs):
        print('--进入闭包函数，开始验证--')
        func(*args,**kwargs)
    return call_func

@test_func
def test(num,*args,**kwargs):
    print(f'--test--{num}')
    print(f'--test--{args}')
    print(f'--test--{kwargs}')

test(10)
test(10,20)
test(10,20,30)
test(10,20,30,test=40)