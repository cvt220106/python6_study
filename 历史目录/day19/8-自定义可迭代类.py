# @Author : 杨佳杰
# @Time   : 2022/6/20 11:38
# @File   : 8-自定义可迭代类.py
from collections.abc import Iterable, Iterator  # 可迭代对象,迭代器


class MyIterator:
    """自定义迭代器,供自定义可迭代对象使用"""

    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    # 迭代器的标志就是有next和iter方法!
    # next方法用于迭代遍历输出可迭代对象
    def __next__(self):
        if self.current < len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    # 迭代器自身也是一个可迭代对象
    def __iter__(self):
        return self


class Mylist:  # 自定义可迭代对象!
    def __init__(self):
        self.container = []

    def add(self, x):
        self.container.append(x)

    def __iter__(self):
        # 只有一个类对象内定义了__iter__,这个对象才是一个可迭代对象
        # 并且返回一个迭代器后,并可对可迭代对象进行for in 遍历
        myiter = MyIterator(self)
        return myiter


my_list = Mylist()
print(isinstance(my_list, Iterable))  # 判断是否为可迭代对象
# iter函数是传入可迭代对象Iterable,得到其背后的迭代器Iterator
print(isinstance(iter(my_list), Iterator))  # 判断是否为迭代器
my_list.add(1)
my_list.add(2)
my_list.add(3)
for i in my_list:
    print(i)
myiter = iter(my_list)  # 得到可迭代对象的迭代器
print(next(myiter))  # 通过next方法利用迭代器获取值
print(next(myiter))
print(next(myiter))
# print(next(myiter))#超出范围,抛出StopIteration异常
