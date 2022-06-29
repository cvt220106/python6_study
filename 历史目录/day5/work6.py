# @Author : 杨佳杰
# @Time   : 2022/6/4 21:51
# @File   : work6.py
# 求两个有序数字列表的公共元素
def find_same_num(lst1,lst2):
    """
    算法思想：由于两个列表均已有序，则可采用双指针来遍历两个列表
    对比双指针i，j所指元素大小，相同则将元素收录与输出列表same_num
    若不相同，则令较小的数所对应指针右移
    遍历结束条件：i或j遍历结束某一个列表
    :param lst1:
    :param lst2:
    :return same_num:
    """
    i=0
    j=0
    l1=len(lst1)
    l2=len(lst2)
    same_num=[]
    while i<l1 and j<l2:
        if lst1[i]==lst2[j]:
            same_num.append(lst1[i])
            i+=1
            j+=1
        elif lst1[i]<lst2[j]:
            i+=1
        else:
            j+=1
    return same_num

list1=[1,2,3,4,5,6,7,8,9]
list2=[2,4,6,7,9,10]
print(find_same_num(list1,list2))



