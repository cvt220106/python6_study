# @Author : 杨佳杰
# @Time   : 2022/6/7 19:44
# @File   : work2-可变参数.py
def demo(lst,dic):
    lst.append('change')
    dic['change']=999
    return

list1=[1,2,3]
dict1={'name':'yang','age':18}
print('改变前'.center(11,'-'))
print(list1)
print(dict1)
demo(list1,dict1)
print('改变后'.center(11,'-'))
print(list1)
print(dict1)
