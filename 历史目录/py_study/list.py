#列表元素的创建
lst=[10,20,30,40,50,60,70,80,90]#直接用[]创建
#利用内置list()函数构建
test=list([10,20,30])
print(test)

'''空列表的创建'''
l1=[]
l2=list()

#列表元素的索引
print(lst[0])#10
print(lst.index(10))#0
#切片操作,得到一个新的列表lst[start:stop:step]
#start:默认0,stop:默认lst最大索引值,step默认1
new_list=lst[2:7:1]
print(lst,id(lst))#[10, 20, 30, 40, 50, 60, 70, 80, 90]
print(new_list,id(new_list))#[30, 40, 50, 60, 70]
#判断与遍历
print(10 in lst)#true
print(10 in new_list)#false
for item in lst:
    print(item)
    '''
    10
    20
    30
    40
    50
    60
    70
    80
    90
    '''
#元素的增加操作
print('------append函数在列表末尾增加一个元素------------')
print('插入前的id',id(lst))
lst.append('hello')
print('插入后的id',id(lst))#append函数在原列表的基础上增加
print(lst)#[10, 20, 30, 40, 50, 60, 70, 80, 90, 'hello']
print('-------extend函数在任意位置上增加至少一个元素')
lst2=['ni','hao','world']
'''
lst.append(lst2)#将列表lst2当做一个元素插入lst
print(lst,id(lst))
'''
lst.extend(lst2)#将lst2中的元素一个个添加至lst尾部
print(lst,id(lst))#[10, 20, 30, 40, 50, 60, 70, 80, 90, 'hello', 'ni', 'hao', 'world']
print('-------insert函数在任意位置上增加一个元素')
lst.insert(1,100)
print(lst,id(lst))#[10, 100, 20, 30, 40, 50, 60, 70, 80, 90, 'hello', 'ni', 'hao', 'world']
print('-------利用切片在任意位置上增加多个元素')
lst3=['beatoful','girl']
lst[1:2]=lst3
print(lst,id(lst))#[10, 'beatoful', 'girl', 20, 30, 40, 50, 60, 70, 80, 90, 'hello', 'ni', 'hao', 'world']

#列表的删除操作
lst.remove('hello')#remove删除指定元素值,若存在相同值,先删除索引值小的元素
print(lst)#[10, 'beatoful', 'girl', 20, 30, 40, 50, 60, 70, 80, 90, 'ni', 'hao', 'world']
lst.pop(1)#pop删除指定索引所对应的元素
print(lst)#[10, 'girl', 20, 30, 40, 50, 60, 70, 80, 90, 'ni', 'hao', 'world']
lst.pop()#若不给出索引值,则默认删除末尾元素值
print(lst)#[10, 'girl', 20, 30, 40, 50, 60, 70, 80, 90, 'ni', 'hao']
lst[1:2]=[]#切片后替换为空,则实现了删除操作
print(lst)#[10, 20, 30, 40, 50, 60, 70, 80, 90, 'ni', 'hao']
lst.clear()#函数清空列表
print(lst)#[]
del lst
'''
print(lst) 删除后lst不存在,print则会异常报错
'''

#列表元素的更新操作
lst=[10,'hello','world','python',50,60,70,80,90]
print(lst)#[10, 'hello', 'world', 'python', 50, 60, 70, 80, 90]
#利用索引值直接修改
lst[1]=20
print(lst)#[10, 20, 'world', 'python', 50, 60, 70, 80, 90]
#利用切片范围修改替换值
lst[2:4]=[30,40]
print(lst)#[10, 20, 30, 40, 50, 60, 70, 80, 90]

#列表的排序
lst1=[100,20,32,53,876,45234,123,4]
#内置函数sort,在原列表的基础上排序,默认升序
print(lst1)#[100, 20, 32, 53, 876, 45234, 123, 4]
lst1.sort()
print(lst1)#[4, 20, 32, 53, 100, 123, 876, 45234]
lst1.sort(reverse=True)#降序排序
print(lst1)#[45234, 876, 123, 100, 53, 32, 20, 4]
#内置sorted函数,原列表不变,生成一个新的有序列表
new_lst1=sorted(lst1)
print(lst1,id(lst1))#[45234, 876, 123, 100, 53, 32, 20, 4],2011161822784
print(new_lst1,id(new_lst1))#[4, 20, 32, 53, 100, 123, 876, 45234],2011161835200

#利用列表生成式建立列表
demo=[i for i in range(1,10)]
print(demo)#生成一个包含1-9元素的列表
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
demo1=[i for i in range(1,10) if i%2==0]
print(demo1)#生成偶数的元素列表
#[2, 4, 6, 8]
demo2=[i*2 for i in range(1,5)]
print(demo2)#效果同demo1
#[2, 4, 6, 8]

# 列表的翻转
