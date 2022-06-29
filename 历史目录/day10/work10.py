# @Author : 杨佳杰
# @Time   : 2022/6/9 21:27
# @File   : work10.py
import os
import sys

def swap_file(filename):
    file=open(filename,'r+',encoding='utf8')
    w=''
    while True:
        text = file.readline().lower()
        if not text:
            break
        for i in text:
            if not i.isalnum() and i != '\n':
                text=text.replace(i,' ')
        w+=text
    file.seek(0,os.SEEK_SET)
    file.write(w)
    file.close()


if __name__=='__main__':
    swap_file(sys.argv[1])




