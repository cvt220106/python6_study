# @Author : 杨佳杰
# @Time   : 2022/6/22 17:53
# @File   : work4-多重继承.py
# 存在多重继承时,防止多继承报错,使用不定长参数,*args,**kwargs来接收参数
class Parent:
    def __init__(self, name, *args, **kwargs):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print('GrandSon的init开始被调用')
        super().__init__(name, age, gender)
        # print(super.mro(self))
        print('GrandSon的init结束被调用')

#通过mro方法得到子类继承时父类的加载顺序
print(GrandSon.__mro__)
gs = GrandSon('yang', 21, '男')
print(gs.name, gs.age, gs.gender)
