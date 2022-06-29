# @Author : 杨佳杰
# @Time   : 2022/6/23 10:04
# @File   : 4-三种property装饰器.py
class Good:
    @property
    def price(self):
        print('property')

    @price.setter#给property属性赋值
    def price(self,value):
        print('price.setter')

    @price.deleter#删除property属性
    def price(self):
        print('price.deleter')

obj=Good()
obj.price#自动执行 @property price 方法
obj.price=100#自动执行 @price.setter 修饰的 price 方法，并将 123 赋
del obj.price# 自动执行 @price.deleter 修饰的 price 方法
