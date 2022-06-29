# @Author : 杨佳杰
# @Time   : 2022/6/7 15:50
# @File   : 5-封装案例2.py
class Gun():
    def __init__(self,model):
        self.model=model
        self.bullet_count=0#子弹数起始为0


    def add_bullet(self,count):
        self.bullet_count+=count


    def shoot(self):
        if self.bullet_count<1:
            print('没有子弹,无法射击')
        self.bullet_count-=1
        print(f'射击成功!当前剩余子弹数为{self.bullet_count}')


    def __str__(self):
        return f'{self.model}还有子弹{self.bullet_count}发'

class Solider():
    def __init__(self,name):
        self.name=name
        self.gun:Gun=None

    def fire(self):
        if self.gun is None:
            print('手里没枪,无法冲锋!')
            return
        print(f'{self.name}手里有枪,冲啊!')
        self.gun.add_bullet(50)
        self.gun.shoot()

    def __str__(self):
        return f'{self.name}手里拿着{self.gun}+'


ak47=Gun('AK47')
xusanduo=Solider('许三多')
xusanduo.gun=ak47
xusanduo.fire()
print(xusanduo)

