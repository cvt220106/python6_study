# @Author : 杨佳杰
# @Time   : 2022/6/20 20:14
# @File   : work3-观察是否为可迭代对象,迭代器.py
from collections.abc import Iterable, Iterator

lst1 = list()
tuple1 = tuple()
dict1 = dict()
set1 = set()

print(isinstance(lst1, Iterable))  # True
print(isinstance(lst1, Iterator))  # False
print(isinstance(iter(lst1), Iterator))  # True

print(isinstance(tuple1, Iterable))  # True
print(isinstance(tuple1, Iterator))  # False
print(isinstance(iter(tuple1), Iterator))  # True

print(isinstance(dict1, Iterable))  # True
print(isinstance(dict1, Iterator))  # False
print(isinstance(iter(dict1), Iterator))  # True

print(isinstance(set1, Iterable))  # True
print(isinstance(set1, Iterator))  # False
print(isinstance(iter(set1), Iterator))  # True
"""
总结:列表.元祖,字典,集合自身都是一个Iterable--即可迭代对象
但需要注意的是,它们自身并不是一个迭代器,是内部嵌有一个迭代器
通过iter(可迭代对象)-->迭代器,便可以得到其内部的迭代器
因此iter()后得到是True
"""