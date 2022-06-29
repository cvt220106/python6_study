# 作者: 王道 龙哥
# 2022年06月07日11时29分37秒
class Person:
    def __init__(self,name,age,height): #初始化方法
        self.name=name
        self.age=age
        self.height=height

    def run(self):
        print(self.name+' is running')

    def eat(self):
        print(f'{self.name} is eatting')

    def __str__(self):#n内置方法
        """
        返回值必须是字符串类型的
        :return:
        """
        info=f'姓名:{self.name},年龄:{self.age},身高:{self.height}'
        return info

    def __del__(self):#删除对象
        print('I will del')

#xiaoming就是一个对象
xiaoming=Person('小明',18,175)
xiaoming.run()
xiaoming.eat()
print(xiaoming.name)

xiaomei=Person('小美',16,165)
xiaomei.run()
print('-'*50)
print(xiaoming)#定义__str__方法后,并可将类按字符串直接输出

xiaogang=Person('小刚',20,188)



print('-'*50)
class Cat:
    """这是一个猫类"""

    def eat(self):
        print("小猫爱吃鱼"+self.name)

    def drink(self):
        self.eat()  #类内部通过self可以调用其他对象方法
        print("小猫在喝水")



tom = Cat()
print(tom)
tom.name='Tom'  #不推荐在 类的外部 给对象增加属性
tom.drink()
tom.eat()
print(tom.name)

