'''元祖的创建'''
#()直接创建
t1=(10,20,30,40)
print(t1)
#利用内置的tuple()函数创建
t2=tuple((10,20,30,40))
print(t2)

'''空元祖的创建'''
t3=()
t4=tuple()

'''元祖是不可变的数据结构,但元祖其中的可变对象可以修改值'''
demo=(10,[20,'yello','red'],90)
print(demo[1],type(demo[1]))
demo[1].append('helloworld')
print(demo)
demo[1][0]='python'
print(demo)

'''元祖的遍历'''
for item in t1:
    print(item)