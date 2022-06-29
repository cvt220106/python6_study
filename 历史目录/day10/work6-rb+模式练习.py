# @Author : 杨佳杰
# @Time   : 2022/6/9 20:37
# @File   : work6-rb+模式练习.py
import os
def test_rbplus():
    """
    r+,已读写形式打开已存在的字符表示的文件
    b附加模式,用于打开不能用字符表示的二进制文件,如图片等
    实现了图片的copy
    :return:
    """
    file=open('v-13.jpg','rb+')
    copy_file=open('copy_photo.jpg','wb')
    content=file.read()
    print(content)#字节流
    copy_file.write(content)
    file.close()
    copy_file.close()


if __name__=='__main__':
    test_rbplus()
