# @Author : 杨佳杰
# @Time   : 2022/6/8 14:48
# @File   : 1-try-except尝试.py
def isymmetric_number(num):
    str1=str(num)
    str2=str1[::-1]
    if str1==str2:
        print(f'{num}是对称数！')
    else:
        raise Exception(f'输入的{num}不是对称数！请重新输入')


try:
    num=int(input('请输入一个整形数：'))
    isymmetric_number(num)
except ValueError:
    print('请输入整数！')
except Exception as result:
    print(result)

