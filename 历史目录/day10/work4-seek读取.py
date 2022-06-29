# @Author : 杨佳杰
# @Time   : 2022/6/9 19:54
# @File   : work4-seek读取.py
import os

file=open('work4','w+',encoding='utf8')
file.write('hello world')
file.seek(5,0)
content=file.read()
print((content))
file.close()
