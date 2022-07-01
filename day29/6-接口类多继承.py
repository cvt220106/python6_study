# @Author : 杨佳杰
# @Time   : 2022/7/1 14:53
# @File   : 6-接口类多继承.py
from abc import abstractmethod, ABCMeta


class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class SwimAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(WalkAnimal, SwimAnimal):
    def swim(self):
        print('tiger swim')

    def walk(self):
        print('tiger walk')


t1 = Tiger()
