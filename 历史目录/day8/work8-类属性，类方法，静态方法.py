# @Author : 杨佳杰
# @Time   : 2022/6/7 22:23
# @File   : work8-类属性，类方法，静态方法.py
class Tools:
    count = 0  # 类属性，记录Tools类工具数

    def __init__(self, name):
        self.name = name
        # 初始化一个对象，工具数加一
        Tools.count += 1

    def use(self):
        print(f'使用{self.name}工具')

    @classmethod#类方法，针对类对象的方法
    def show_tool_count(cls):
        print(f'当前有{cls.count}个工具对象')#类方法内通过cls访问类属性或其他类方法

    @staticmethod#静态方法，无需访问其他属性与方法，一般打印帮助说明
    def help():
        print('这是一个工具对象类！')


Tools.help()#通过类名调用静态方法
tool1=Tools('锤子')
tool2=Tools('椅子')
tool3=Tools('火柴')
Tools.show_tool_count()#通过类名调用类方法

"""
类属性，在class直接定义，用于记录该类的一些特征，通过类名直接访问
类方法，需申明@classmethod后再定义，可在类方法中访问类属性与类方法，通过补全的cls引用类名访问其他
外部访问类方法时，直接使用类名访问，无需参数
静态方法，需申明@staticmethod后再定义，静态方法在外部也是通过类名来访问，并且静态方法内部不访问其他属性与方法
外部调用时也无需参数
"""