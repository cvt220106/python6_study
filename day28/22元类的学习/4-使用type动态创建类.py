Test2 = type('Test', (), {})
"""
第一个参数为类名
第二个参数()内写入该类所继承的父类名,默认为object
第三个参数{}内写入的是该类中类方法,类属性的键值对
所以这个type创建语句等同于
class Test:
    pass
"""
print(Test2)
# help方法可以输出对应类的各种属性
print(help(Test2))
print('-' * 50)
print('----使用type创建带有属性的类')
Foo = type('Foo', (), {'bar': True})
"""等同于
class Foo:
    bar=True
"""
print(Foo.bar)
f = Foo()
print(f)

print('-' * 50)
print('----使用type创建带有方法的类')


def echo_bar(self):
    print(self.bar)


# 利用type定义类并定义类方法echo_bar
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})  # FooChild继承了父类Foo
print(help(FooChild))

print(hasattr(Foo, 'echo_bar'))

print(hasattr(FooChild, 'echo_bar'))  # 判断FooChild类中 是否有echo_bar这个属性

f1 = FooChild()
f1.echo_bar()

print('-' * 100)


@staticmethod
def test_static():
    print("static method ....")


@classmethod
def test_class(cls):
    print(cls.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar, 'test_static': test_static
    , 'test_class': test_class})

f2 = FooChild()
f2.test_static()
f2.test_class()
