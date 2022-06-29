#定义一个类
class Student:
    native_place='武汉'#所有该类对象所共有的属性--类属性
    def __init__(self,name,age,grade):#初始化类的实例属性,即name,age,grade
        self.name=name
        self.age=age
        self.grade=grade
    
    #定义实例方法
    def info(self):
        print(f'我叫{self.name},我今年{self.age}岁,本次考试取得了{self.grade}分的成绩')
    #定义类方法
    @classmethod
    def cm(cls):
        print('这是类方法,因为我使用了@classmethod!')
    #定义静态方法
    @staticmethod
    def sm():
        print ('这是静态方法,因为我使用了@staticmethod!')

'''创建Student类实例对象'''
stu1=Student('张三',20,98)
stu2=Student('李四',21,78)
#实例属性的输出
print(stu1.name,stu1.age,stu1.grade)
print(stu2.name,stu2.age,stu2.grade)
#实例方法的两种调用方式
stu1.info()
Student.info(stu1)

'''类属性,类方法,静态方法的使用'''
#类属性的使用方法,类中方法外的属性称为类属性,为所有的该类所共享
print(Student.native_place)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='黄冈'
print(stu1.native_place)
print(stu2.native_place)
#类方法,静态方法的调用.均为类名直接访问
Student.cm()
Student.sm()

''''动态绑定类的属性与方法'''
stu1.gender='男'
print(stu1.name,stu1.age,stu1.grade,stu1.gender)
#print(stu2.name,stu2.age,stu2.grade,stu2.gender)
#出现异常报错,因为stu2并未动态绑定gender属性

def study(self):#定义在类外称作函数
    print(f'{self.name}正在学习')
Student.study=study#将study函数绑定至Student类,则为其实例方法
stu1.study()
stu2.study()