# @Author : 杨佳杰
# @Time   : 2022/6/23 10:22
# @File   : 5-实战三种property.py
class Goods:
    def __init__(self):
        self.originnal_price=100
        self.discount=0.8

    @property
    def price(self):
        return self.originnal_price*self.discount

    @price.setter
    def price(self,value):
        self.originnal_price=value

    @price.deleter
    def price(self):
        del self.originnal_price


gas=Goods()
print(gas.price)
gas.price=200
print(gas.price)
del gas.price
# print(gas.originnal_price)