# @Author : 杨佳杰
# @Time   : 2022/6/9 15:24
# @File   : 文件及目录操作.py
import os
import sys


def use_file():
    os.rename('dir/file2','dir/file1')


def use_remove():
    os.remove('dir/dir2/file1')


def use_dir():
    print(os.listdir('dir'))
    #os.remove('dir/dir2')#remove不能用来删文件夹
    #os.rmdir('dir/dir2')#文件夹采用rmdir删除
    #os.mkdir('dir/dir2')#mkdir创建目录
    print(os.getcwd())#getcwd获取当前工作目录的地址
    os.chdir('dir')#chdir修改工作目录
    print(os.getcwd())
    print(os.path.isdir('file1'))#path.isdir判断是否为目录
    print(os.path.isdir('dir2'))


def dfs(path_name,width):
    file_names=os.listdir(path_name)
    for i in file_names:
        print(' '*width+i)#打印文件名
        current_name=path_name+'/'+i
        if os.path.isdir(current_name):
            dfs(current_name,width+4)


def python_argv():
    """
    python文件传参
    :return:
    """
    print(len(sys.argv))
    print(sys.argv)#sys.argv[0]

if __name__=='__main__':
    dfs(sys.argv[1],0)
    #use_file()
    #use_remove()
    #use_dir()
    #python_argv()
