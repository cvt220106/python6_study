# @Author : 杨佳杰
# @Time   : 2022/6/23 22:49
# @File   : work2-魔法属性.py
class TestDoc:
    """doc就是这个类的简介"""
    def test(self):
        pass

#__doc__魔法属性:输出类内""""""的描述简介信息
print(TestDoc.__doc__)
print('-'*50)

from test import Person

obj=Person()
#__module__魔法属性.输出该类所在的模块名
print(obj.__module__)
#__class__魔法属性,输出实例对象对应类名,效果同于type
print(obj.__class__)
print(type(obj))
print('-'*50)

class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def __call__(self, *args, **kwargs):
        print('__call__')

    def __str__(self):
        return '__str__属性就是输出实例化对象时,输出这个返回值'

#__init__魔法属性,在创建实例化对象时自动调用执行
f=Foo('yang',21)
#__call__魔法属性,在实例化对象加()触发执行
f()
print('-'*50)

#__dict__魔法属性,输出类或实例对象的全部属性和方法
print(Foo.__dict__)#Foo的全部属性和方法
print(f.__dict__)#f这个实例化对象的属性
print('-'*50)

#__str__魔法属性,在打印对象时，默认输出该方法的返回值。
print(f)