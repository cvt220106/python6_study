# @Author : 杨佳杰
# @Time   : 2022/6/30 16:12
# @File   : 1-类也可以传递.py
class ObjectCreator:
    pass


def echo(obj):
    print(obj)
    obj.new_attribute = 'foo'
    print(obj())  # 通过ObjectCreator类创建了一个实例对象


echo(ObjectCreator)
print(ObjectCreator.new_attribute)
# hasattr(__obj,__name),判断一个类中是否存在对应属性
print(hasattr(ObjectCreator, 'new_attribute'))


