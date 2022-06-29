# @Author : 杨佳杰
# @Time   : 2022/6/6 10:53
# @File   : 3-列表联系.py
list1=[1,2,3]
list2=[7,8,9]
#索引
print(list1[0])
print(list1.index(2))


a=[j for i in range(10) for j in range(i)]
print(a)
b=[[col*row for col in range(5)] for row in range(5)]#二维列表
print(b)
c=[j for x in b for j in x]#二维转一维
print(c)

x=10
y=5
maxnum=x if x>y else y
print(maxnum)

t1=(1,2,3)
l1=list(t1)
print(l1)

l2=[1,2,3,4,5]
l3=list(reversed(l2))
print(l3)
l4=[2,4,6]
l2[::2]=l4
print(l2)
print(l2.count(9))
l5=sorted(l2,reverse=True)
print(l5)
t1=()
print(type(t1))