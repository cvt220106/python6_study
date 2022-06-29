# @Author : 杨佳杰
# @Time   : 2022/6/13 20:29
# @File   : 4-sorted的使用.py
'''
sorted[可迭代对象,key=,reverse=False]
key对应控制排序时对应排序变量选取
reverse对应控制排序结果为升序还是降序,默认为升序
'''
# 1sorted直接对可迭代进行排序,排序结果返回一个新的列表,原迭代对象不变
list1 = [2, 6, 3, 4, 1, 7]
print(sorted(list1))
print(list1)  # list1并未发生变化
# 相较于列表自带的sort函数,sort函数是在愿列表的基础本身进行排序,并且只对列表有效
list1.sort()
print(list1)

print('-' * 50)
# 2sorted对其他可迭代对象进行排序
str1 = 'afjuioqwclopq'
print(sorted(str1))  # 返回值为一个列表
dic1 = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(dic1))  # 字典的排序元素为字典内的key,返回值为key值排序后生成的列表
print('-' * 50)
# 3引入key参数,用一个函数得到指定形式的参数进行排序
lst1 = "This is a test string from Andrew".split()
# 对列表中的字符串元素进行排序
print(sorted(lst1, key=str.lower))  # key参数传入lower处理过的排序对象进行排序
print('-' * 50)
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# 对列表中的元祖进行排序,利用lambda匿名函数,选择元组内对应元素排序
print(sorted(student_tuples, key=lambda student: student[0]))
print(sorted(student_tuples, key=lambda student: student[1]))
print(sorted(student_tuples, key=lambda student: student[2]))
print('-' * 50)



class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):  # 对打印进行重写,并且可以输出元祖类型
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10)]
# 对类对象进行排序,在key中直接指明进行排序的实例对象属性
print(sorted(student_objects,key=lambda student:student.name))
print(sorted(student_objects,key=lambda student:student.grade))
print(sorted(student_objects,key=lambda student:student.age))
print('-'*50)

#4引入库函数,更加便捷的使用key
from operator import itemgetter, attrgetter
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_tuples, key=itemgetter(1)))
print(sorted(student_tuples, key=itemgetter(2)))#itemgetter指定元祖,字典类中的元素下标进行排序
print('-'*50)
print(sorted(student_objects, key=attrgetter('name')))
print(sorted(student_objects, key=attrgetter('grade')))
print(sorted(student_objects, key=attrgetter('age')))#attrgetter对类对象属性指定排序
print('-'*50)
#多层排序,先依据一个属性排序,再依据另外一个排序
print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_objects, key=attrgetter('grade', 'age')))
print('-'*50)
#5字典内value值内嵌列表进行排序
mydict = {'Li' : ['M',7],'Zhang': ['E',2],'Wang' : ['P',3],
            'Du' : ['C',2],'Ma' : ['C',9],'Zhe' : ['H',7] }
print(sorted(mydict.items(), key=lambda v: v[0]))#利用字典的key值排序
print(sorted(mydict.items(), key=lambda v: v[1][0]))#利用字典value值中的列表的第一个元素进行排序
print(sorted(mydict.items(), key=lambda v: v[1][1]))#利用字典value值中的列表的第二个元素进行排序
print('-'*50)
#6列表嵌套字典元素进行排序
gameresult = [
{ "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
{ "name":"David", "wins":3, "losses":5, "rating":57.00 },
{ "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
{ "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
print(sorted(gameresult , key=itemgetter("rating","name")))#先根据rating排序,rating相同时再根据姓名排序




