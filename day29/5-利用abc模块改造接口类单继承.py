# @Author : 杨佳杰
# @Time   : 2022/7/1 11:35
# @File   : 5-利用abc模块改造接口类单继承.py
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    # 抽象方法是需要子类来实现的方法,若子类未实现对应名方法,则会在创建实例对象时便发生报错
    def pay(self, money):
        pass


class Alipay(Payment):
    def paying(self, money):
        # 发生报错:Can't instantiate abstract class Alipay with abstract method pay
        print(f'支付宝支付了{money}')


class Apppay(Payment):
    def pay(self, money):
        print(f'苹果支付了{money}')


class Wechatpay(Payment):
    def pay(self, money):
        print(f'微信支付了{money}')


def pay(payment, money):
    payment.pay(money)


p = Alipay()  # 实例化对象时触发拦截判断
