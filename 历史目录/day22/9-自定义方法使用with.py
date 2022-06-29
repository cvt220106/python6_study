# @Author : 杨佳杰
# @Time   : 2022/6/23 14:33
# @File   : 9-自定义方法使用with.py
from contextlib import contextmanager

@contextmanager
def my_open(path,mode):
    f=open(path,mode)
    yield f
    print('file will close')
    f.close()

with my_open('file.txt','r') as f:
    print(f.read())