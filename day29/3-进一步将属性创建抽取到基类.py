# @Author : 杨佳杰
# @Time   : 2022/7/1 10:50
# @File   : 3-进一步将属性创建抽取到基类.py
# 元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs: dict):
        mappings = dict()
        for key, value in attrs.items():
            if isinstance(value, tuple):
                print('Found mapping: %s ==> %s' % (key, value))
                mappings[key] = value

        # 删除存在于mappings中的属性
        # 为了用户创建时直接当做类属性创建,而后层再处理不影响整体,从而使用起来更简洁
        for key in mappings.keys():
            attrs.pop(key)

        # 保存属性与数据表字段名的映射关系
        attrs['__mappings__'] = mappings
        # 假设数据表名与类名相同
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)
        # return type(name,bases,attrs) # 只会单次进入ModelMetaclass,不会拦截子类的创建


class Model(metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        # 使用不同的判别技术,来判断value的值是否带上引号
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        sql = f"""insert into {self.__table__}({','.join(fields)}) """ \
              f"""values({','.join(["'" + i + "'" if isinstance(i, str) else str(i) for i in args])})"""

        print(sql)


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('name', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')


u = User(uid=12345, name='Michael', email='test@orm.org', password='mypwd')
u.save()
