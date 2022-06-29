# @Author : 杨佳杰
# @Time   : 2022/6/7 10:58
# @File   : 2-递归.py
def f(n):
    if n==1:
        return 1
    return n+f(n-1)

print(f(5))

print('-'*50)
def jieti(n):
    if n==1 or n==2:
        return n
    list1=[0]*(n+1)
    list1[1]=1
    list1[2]=2
    i=3
    while i<=n:
        list1[i]=list1[i-1]+list1[i-2]
        i+=1
    return list1

print(jieti(10))
