# @Author : 杨佳杰
# @Time   : 2022/6/20 14:46
# @File   : 9-生成器实现斐波那契.py
# def+yield==generator
def fib(n):
    num1,num2=0,1
    current=0
    while current<n:
        num=num1
        num1,num2=num2,num1+num2
        current+=1
        yield num
    return -1


F=fib(5)
print(F)#<generator object fib at 0x000001D082CD2960>
#生成器采用next方法唤醒
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print('-'*50)
try:
    print(next(F))
except Exception as e:
    print(e)#