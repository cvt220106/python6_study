# @Author : 杨佳杰
# @Time   : 2022/7/1 9:45
# @File   : 1-metaclass生成类.py
# 使用type.__new__重写new方法时,要继承type为父类
class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parent, class_attr: dict):
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith('__'):
                new_attr[name.upper()] = value

        # return type(class_name, class_parent, new_attr)
        # 可以保证父类使用metaclass正确
        return type.__new__(cls, class_name, class_parent, new_attr)


class Foo(metaclass=UpperAttrMetaClass):
    bar = 'bip'


print(Foo.BAR)


class FooChild(Foo):
    pass


print(FooChild.BAR)
