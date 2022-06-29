# @Author : 杨佳杰
# @Time   : 2022/6/23 14:11
# @File   : 7-with的使用.py
def m2():
    file = open('file.txt', 'r', encoding='utf8')
    try:
        file.write('hello world')
    except IOError:
        print('oops error')
    finally:
        file.close()

def m3():
    with open('file.txt','w',encoding='utf8') as f:
        f.write('hello')
    #with会自动将打开文件进行关闭
    print(f.read())#ValueError: I/O operation on closed file


if __name__ == '__main__':
    # m2()
    m3()