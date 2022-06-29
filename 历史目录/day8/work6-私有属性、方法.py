# @Author : 杨佳杰
# @Time   : 2022/6/7 19:56
# @File   : work6-私有属性、方法.py
class Women:
     def __init__(self,name):
         self.name=name
         self.__age=18#私有属性

     def __secret(self):#私有方法，通过私有方法访问私有属性
         print(f'{self.name}的年龄是{self.__age}')

     def boyfriend(self):#再通过公有方法调用私有方法，从而达到输出私有属性的操作
         self.__secret()

xiaomei=Women('小美')
#print(xiaomei.__age)# 私有属性外部无法直接访问
#xiaomei.__secret()#私有方法外部无法直接调用
xiaomei.boyfriend()