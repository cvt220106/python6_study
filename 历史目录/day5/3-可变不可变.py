# @Author : 杨佳杰
# @Time   : 2022/6/4 11:21
# @File   : 3-可变不可变.py
"""
无论可变不可变类型,再次赋值与上次不同,则id一定会变

"""
a=1
print(id(a))
a='hello'
print(id(a))
a=[1,2,3]
print(id(a))
a=[3,2,1]
print(id(a))

demo=[1,2,3]
print(f'列表插入前地址为{id(a)}')
demo.append(999)
print(f'列表插入后地址为{id(a)}')

