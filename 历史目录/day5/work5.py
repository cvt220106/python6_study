# @Author : 杨佳杰
# @Time   : 2022/6/4 21:24
# @File   : work5.py
# 局部变量与全局变量

def test1():
    i = 5
    print(f'test1函数中，地址为{id(i)}')


# test函数中i即使赋值5，与外部的全局变量相同都叫i，但二者并无关联
# 函数中的变量称作局部变量，局部变量的赋值改变不影响全局变量的改变
def test2():
    global i
    print(f'test2函数中修改前，地址为{id(i)}')
    i=5
    print(f'test2函数中修改后，地址为{id(i)}')


# 在函数中申明global变量则可以在函数中改变全局变量

i = 10
print(f'初始地址为{id(i)}')
test1()
print(f'test1函数后，i的值为{i}，地址为{id(i)}')
test2()
print(f'test2函数后，i的值为{i}，地址为{id(i)}')
