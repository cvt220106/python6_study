# @Author : 杨佳杰
# @Time   : 2022/6/23 9:50
# @File   : 2-property属性.py
class Foo:
    def func(self):
        print('I am func')

    @property#装饰器
    def prop(self):
        print('I am prop')


f=Foo()
f.func()
f.prop#当做属性直接调用!
print('-'*50)
class Good:
    @property
    def size(self):
        return 100


good=Good()
width=good.size
print(width)