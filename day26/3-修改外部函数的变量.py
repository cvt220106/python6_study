# @Author : 杨佳杰
# @Time   : 2022/6/28 16:24
# @File   : 3-修改外部函数的变量.py
x=300 # global

def test1():
    x=200 # nonlocal
    def test2():
        nonlocal x
        print(f'-----1-------x={x}')# 输出200
        x=100 # 一旦修改就必须在使用前添加修饰
        print(f'-----2-------x={x}')

    return test2


t=test1() # 拿到闭包的入口地址
t() # 运行闭包函数


# 外部函数中的形参也是nonloca类型
def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr


c1 = counter(5)
print(c1())
print(c1())
c2 = counter(50)
print(c2())
print(c2())