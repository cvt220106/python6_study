# @Author : 杨佳杰
# @Time   : 2022/6/23 14:23
# @File   : 8-自定义with.py
class File:
    """
    任何实现了 __enter__() 和 __exit__() 方法的对象都可称之为上下文管理器
    上下文管理器对象可以使用 with 关键字
    """
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        """返回as后的对象"""
        self.f=open(self.filename,self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('I will exit')
        self.f.close()


with File('context.txt','w') as f:
    print('writing')
    f.write('这是在测试!')
# I will exit 的输出表明了__exit__的调用,以及f.close的执行

