# @Author : 杨佳杰
# @Time   : 2022/6/9 19:18
# @File   : work3-读取文件并复制.py
import os

def small_file_copy(filename,copy_filename):
    file=open(filename,'r',encoding='utf8')
    copy_file=open(copy_filename,'w',encoding='utf8')
    content=file.read()
    copy_file.write(content)
    file.close()
    copy_file.close()


def big_file_copy(filename,copy_filename):
    file=open(filename,'r',encoding='utf8')
    copy_file=open(copy_filename,'w',encoding='utf8')
    while True:
        content=file.readline()
        if not content:
            break
        copy_file.write(content)
    file.close()
    copy_file.close()

if __name__=='__main__':
    #small_file_copy('Readme','Readme1')
     big_file_copy('BigFile','BigFile1')