# @Author : 杨佳杰
# @Time   : 2022/6/28 16:43
# @File   : 4-装饰器实现原理.py
def set_func(func):
    print('--开始进行装饰--')#1即使不调用test1(),也会执行,在@时就执行了
    def call_func(*args,**kwargs):
        print('---权限验证----')#2
        func(*args,**kwargs)#3
    return call_func

@set_func  #装饰器相当于执行了 test1=set_func(test1)
def test1(num):
    print(f'----test1----{num}')

test1(3)