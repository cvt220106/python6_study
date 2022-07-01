# @Author : 杨佳杰
# @Time   : 2022/7/1 11:24
# @File   : 4-接口类单继承.py
class Alipay:
    def pay(self, money):
        print(f'支付宝支付了{money}')


class Apppay:
    def pay(self, money):
        print(f'苹果支付了{money}')


class Wechatpay:
    def pay(self, money):
        print(f'微信支付了{money}')


def pay(payment, money):
    payment.pay(money)


p = Alipay()
pay(p, 200)
