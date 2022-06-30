#object 是基类，python中所有类都默认继承该类
def upper_attr(class_name, class_parents, class_attr:dict):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()]=value

    return type(class_name, class_parents,new_attr)


class Foo(metaclass=upper_attr):
    bar = 'bip'

print(Foo.BAR)