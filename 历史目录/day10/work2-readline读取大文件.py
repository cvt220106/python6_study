# @Author : 杨佳杰
# @Time   : 2022/6/9 19:33
# @File   : work2-readline读取大文件.py
import os

file=open('BigFile','r',encoding='utf8')
while True:
    content=file.readline()
    if not content:
        break#未读到内容时退出
    #读取一行时会读取到一个换行符,而print也会再打印一个换行符,从而造成多打印一个空行
    print(content,end='')#换为end='',从而完整打印
file.close()