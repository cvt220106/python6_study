# @Author : 杨佳杰
# @Time   : 2022/6/7 14:19
# @File   : 3-类封装.py
class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight


    def __str__(self):
        return f'{self.name}的体重是{self.weight}公斤'


    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight-=0.5


    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight+=1


xiaoming=Person('小明',77)
xiaoming.eat()
print(xiaoming)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)

print('-'*50)
xiaomei=Person('小美',50)
xiaomei.run()
print(xiaomei)
xiaomei.eat()
print(xiaomei)