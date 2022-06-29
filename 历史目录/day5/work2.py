# @Author : 杨佳杰
# @Time   : 2022/6/4 20:05
# @File   : work2.py
# 写一个say_hello函数打印多次hello并给该函数加备注（具体打印几次依靠传递的参数）
# 然后调用say_hello，同时学会快速查看函数备注快捷键，及如何跳转到函数实现快捷键
def say_hello(num):
    """
    这是一个函数,可以实现多次打印hello
    打印次数由函数形参num所控制
    :param num:
    :return:
    """
    for i in range(num):
        print('hello')
    return

say_hello(2)