# @Author : 杨佳杰
# @Time   : 2022/6/7 20:53
# @File   : work7-继承.py
class Animals:
    def eat(self):
        print('吃东西~~')

    def drink(self):
        print('喝水~~')

    def run(self):
        print('奔跑~~')

    def sleep(self):
        print('睡觉~~')

class Dog(Animals):
    def bark(self):
        print('汪汪~~')

class Immortal:
    def spell(self):
        print('神仙会法术！')


class XiaoTianQuan(Dog,Immortal):
    def fly(self):
        print('飞天')

    def bark(self):#对父类进行重写
        print('像人一样说话！')
        print('-'*50)
        super().bark()#使用super调用重写前的父类的方法


xtq=XiaoTianQuan()
xtq.bark()
xtq.eat()#继承Animal父类的方法
xtq.spell()#继承Immortal父类的方法
print(XiaoTianQuan.mro())