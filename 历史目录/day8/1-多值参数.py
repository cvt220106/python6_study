# @Author : 杨佳杰
# @Time   : 2022/6/7 9:56
# @File   : 1-多值函数.py
def demo1(*args,**kwargs):
    print(args)
    print(kwargs)


def demo(num,*args,**kwargs):
    demo1(*args,**kwargs)
    #print(num)


demo(1,2,3,4,5,name='yang',age=18)
tuple1=(2,3,4,5)
dict1={'name':'yang','age':18}
demo(2,*tuple1,**dict1)#拆包