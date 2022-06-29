# @Author : 杨佳杰
# @Time   : 2022/6/23 9:43
# @File   : 1-回顾类.py
class Province:
    country='中国'
    def __init__(self,name):
        self.name=name


taiwan=Province('台湾省')
#输出对象所属类
print(taiwan.__class__)
print(type(taiwan))