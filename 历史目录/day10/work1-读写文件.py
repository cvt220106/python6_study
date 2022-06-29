# @Author : 杨佳杰
# @Time   : 2022/6/9 19:13
# @File   : work1-读写文件.py
import os
#r+模式为读写打开文件,文件不存在时会报错
filename=open('Readme','r+',encoding='utf8')
filename.write('人生苦短,我用python')
filename.close()
