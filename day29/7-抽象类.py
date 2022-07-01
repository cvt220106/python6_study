# @Author : 杨佳杰
# @Time   : 2022/7/1 11:47
# @File   : 8-抽象类.py
"""
1.多继承问题 在继承抽象类的过程中，我们应该尽量避免多继承；
  而在继承接口的时候，我们反而鼓励你来多继承接口
2.方法的实现 在抽象类中，我们可以对一些抽象方法做出基础实现；
  而在接口类中，任何方法都只是一种规范，具体的功能需要子类实现
"""
from abc import abstractmethod, ABCMeta


class Person(metaclass=ABCMeta):
    # 定义抽象方法,无需具体实现
    # 子类必须具有同名方法,并进行具体实现
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fire(self):
        pass


# p=Person()  # 抽象类不能创建实例化对象!


class MeleePerson(Person):
    def walk(self):
        print('近战走路比较快')

    def fire(self):
        print('近战攻击距离比较短')


class RemotePerson(Person):
    def walk(self):
        print('远程走路比较慢')

    def fire(self):
        print('远程攻击距离比较长')


