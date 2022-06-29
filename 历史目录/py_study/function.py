from ast import arg


def func(a,b,c):
    print(a,b,c)

func(10,20,30)#位置实参
func(a=10,c=30,b=20)#关键字实参
lst=[10,20,30]
func(*lst)#将序列中的值转为位置实参,加*
tuple=(10,20,30)
func(*tuple)#元祖同理
set={10,20,30}
func(*set)#集合也同理
dict1={'a':10,'b':20,'c':30}
func(**dict1)#将字典中的键值对转化为关键字实参

def func1(a,b=10):#b为默认值形参,若调用时未输入,则取默认值
    print(a,b)

func1(10)
func1(10,20)#输入时则取输入值
'''若要求形参值得传入必须用关键字实参传入,则在形参处加*'''
def func2(*,a,b,c):
    print(a,b,c)

#func2(10,20,30)位置实参调用函数则会发生报错
func2(a=10,b=20,c=30)
dict2=dict(a=10,b=20,c=30)
print(dict2)
func2(**dict1)

'''位置实参个数可变,定义时加*'''
def func3(*arge):
    print(type(arge))#tuple,以元祖类型存储
    print(arge)

func3(10,20,30,40,50,60)
func3('hello','world')

'''关键字实参个数可变,定义时加**'''
def func4(**arge):
    print(type(arge))#dict,以字典类型存储
    print(arge)

func4(a=10,b=20,c=30,d=40)
func4(name='yang',age=20,grade=398)

print('------------------------')
'''递归函数写斐波那契数列'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))
print('----------------')
for i in range(1,7):
    print(fib(i),end=' ')
