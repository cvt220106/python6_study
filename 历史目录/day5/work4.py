# @Author : 杨佳杰
# @Time   : 2022/6/4 20:56
# @File   : work4.py
def change_or_not():
    i=10
    f=3.1415
    bol=False
    string='world'
    tup=(3,2,1)
    lst.append(100)
    dicts['zhang']=95
    return

i=5
f=3.14
bol=True
string='hello'
tup=(1,2,3)
lst=[1,2,3]
dicts={'yang':100,'wang':87}
print('步入函数前---------')
print(f'i的值为{i}，地址为{id(i)}')
print(f'f的值为{f}，地址为{id(f)}')
print(f'bol的值为{bol}，地址为{id(bol)}')
print(f'string的值为{string}，地址为{id(string)}')
print(f'tup的值为{tup}，地址为{id(tup)}')
print(f'lst的值为{lst}，地址为{id(lst)}')
print(f'dicts的值为{dicts}，地址为{id(dicts)}')
change_or_not()
print('步入函数后---------')
print(f'i的值为{i}，地址为{id(i)}')
print(f'f的值为{f}，地址为{id(f)}')
print(f'bol的值为{bol}，地址为{id(bol)}')
print(f'string的值为{string}，地址为{id(string)}')
print(f'tup的值为{tup}，地址为{id(tup)}')
print(f'lst的值为{lst}，地址为{id(lst)}')
print(f'dicts的值为{dicts}，地址为{id(dicts)}')