# @Author : 杨佳杰
# @Time   : 2022/6/22 17:43
# @File   : work3-工厂模式.py
class Animal():

    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

    def voice(self):
        print('狗叫汪汪')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

    def voice(self):
        print('猫叫喵喵')


# 工厂模式--即实现创建一个对应类时,可以采用对应的字符串来实现对应的实例化对象
class FactoryMode():
    def __init__(self):
        self.factory = {'dog': Dog, 'cat': Cat}

    def create_ani(self, animal_name):
        return self.factory[animal_name]()


f = FactoryMode()
animal1 = f.create_ani('dog')
animal1.eat()
animal1.voice()
animal2=f.create_ani('cat')
animal2.eat()
animal2.voice()
