# @Author : 杨佳杰
# @Time   : 2022/6/6 11:45
# @File   : 4-字典操作.py
dic1={'name':'yang','age':10,'height':178}
dic2={'name':'wang','age':19,'gpa':3.14}
print(id(dic1))
dic1.update(dic2)
print(dic1)
print(id(dic1))
l1=['name','age','gpa']
dict3=dic1.fromkeys(l1,13)
print(dict3)
while dic1:
    print(dic1.popitem())

print(dic2.setdefault('height',178))
print(dic2)

l1=('spring','summer','fall','winter')
l2=enumerate(l1)
dic3={'name':'yang'}
dic3['age']=18
print(dic3)
dic3['age']=19
print(dic3)
dic3.setdefault('age',20)
print(dic3)


list1=['A','B','C','D','E','F','G','H']
dict1={}
dict1=dict1.fromkeys(list1,0)
print(dict1)