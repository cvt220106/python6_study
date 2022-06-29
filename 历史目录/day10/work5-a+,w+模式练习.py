# @Author : 杨佳杰
# @Time   : 2022/6/9 20:10
# @File   : work5-a+,w+模式练习.py
import os

def test_rplus():
    """
    r+模式下,文件不存在时open,会发生报错
    :return:
    """
    file=open('file1','r+',encoding='utf8')
    file.write('test')
    file.seek(0,os.SEEK_CUR)#又读又写时刷新指针
    content=file.read()
    print(content)
    file.close()


def test_wplus():
    """
    w+模式下,文件不存在,则创建文件并写入
    但文件存在时,会覆盖原文件的内容
    :return:
    """
    file=open('file1','w+',encoding='utf8')
    file.write('hello')
    file.seek(0,os.SEEK_SET )
    print(file.read())
    file.close()


def test_aplus():
    """
    a+模式下,文件不存在时,创建文件并写入
    文件存在时,从文件末尾以追加形式写入
    :return:
    """
    file = open('file1', 'a+', encoding='utf8')
    file.write('hello')
    file.close()


if __name__=='__main__':
    #test_rplus()
    #test_wplus()
    test_aplus()