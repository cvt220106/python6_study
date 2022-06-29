# @Author : 杨佳杰
# @Time   : 2022/6/7 19:48
# @File   : work3-缺省参数.py
def demo(name,age,height,gpa=4.0,gender=True):
    print(f'{name}年龄{age}，身高{height},绩点{gpa}')
    if gender:
        print('男生')
    else:
        print('女生')

demo('yang',18,178)
demo('wang',18,175,gender=False)#多个缺省要指明对象
demo('zhang',20,170,3.0)
demo('shi',22,166,3.8,False)