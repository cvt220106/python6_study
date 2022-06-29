# @Author : 杨佳杰
# @Time   : 2022/6/3 22:14
# @File   : work5.py
# 有101个整数，其中有50个数出现了两次，1个数出现了一次， 找出出现了一次的那个数。
# （大家使用7个数即可）
def find_single_num(lst):
    result=0
    for i in lst:
        result^=i
    return result

lst1=[2,1,3,2,1,3,4]
print(find_single_num(lst1))




