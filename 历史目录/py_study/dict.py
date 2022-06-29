'''字典的创建方式'''
#利用{}直接创建
dict1={'张三':83,'李四':92,'王五':69}
print(dict1,type(dict1))
#利用dict()函数创建
dict2=dict(张三=83,李四=92,王五=69)
print(dict2,type(dict2))
#利用zip()函数将两个可迭代对象形成一个字典
names=['张三','李四','王五']
scores=[83,92,69]
dict3={name:score for name,score in zip(names,scores) }
print(dict3,type(dict3))

'''空字典的创建'''
d1={}
d2=dict()

''' 字典元素的读取'''
#[key]直接获取value值
print(dict1['张三'])
#利用get()函数获取
print(dict1.get('张三'))
'''二者的区别
[key]中key若不存在于dict中,会出现报错
get(key)中key若不存在则会默认返回None
get(key,value)则可以实现,查找到改不存在的key值,返回指定的value值
'''
print(dict1.get('陈六'))#None
print(dict1.get('杨',100))#100

'''字典元素的视图'''
print(dict1.keys())#单独获取字典的key值视图
print(type(dict1.keys()))
print(dict1.values())#单独获取字典的value值视图
print(type(dict1.values()))
print(dict1.items())
'''也可用list()将这几种数据结构转化为list'''
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

'''字典的增删改'''
dict1['杨']=100#增加
print(dict1)
dict1['张三']=10#修改
print(dict1)
del dict1['杨']#删除
print(dict1)

'''字典的遍历'''
for item in dict1:
    print(item,dict1[item])