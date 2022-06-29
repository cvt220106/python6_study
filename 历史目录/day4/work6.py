# @Author : 杨佳杰
# @Time   : 2022/6/3 22:24
# @File   : work6.py

def find_two_single_num(lst):
    """
    :param lst:
    :return [a.b]:
    找出两个各只出现一次的数
    算法思想:1.整个lst中数异或的结果即为a^b
    2.由于a与b不同因此异或结果二进制结果中必存在一位为1,而这一位是由a,b中对应位置的1与0
    所得到,如a为1,b为6时,0001^0110=0111,最低位为1,可记此数为c=0b0001
    3.再利用按位与的特点,同1为1,其余为0,因此a,b与c之间按位与必有一个为0,一个不为0,从而分出a,b到不同处理单元
    4.而lst中其他数与c按位与同样被分流开来,但这些数均出现两次,因此两个处理单元均异或后即可得到a,b
    """
    num = 0
    for i in lst:
        num ^= i  # 得到a^b的结果
    c = 1  # 按1,2,4,8..递增与num按位与(同1为1,其余为0)来探测出a,b不同的位数
    while (num & c) == 0:
        c <<= 1  # 找出最低位为1的值,不循环法:a&-a即可得
    a = 0
    b = 0
    for i in lst:
        if i & c == 0:  # 按位与为0为一处理单元
            a ^= i
        else:  # 按位与不为0为一处理单元
            b ^= i
            # a,b在不同处理单元
    result = [a, b]
    return result


lst1 = [2, 4, 2, 1, 3, 4, 3, 9]
print(find_two_single_num(lst1))
