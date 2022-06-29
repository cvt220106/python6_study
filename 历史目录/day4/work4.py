# @Author : 杨佳杰
# @Time   : 2022/6/3 20:41
# @File   : work4.py
# 统计一个整数对应的二进制数的1的个数。
# 输入一个整数（可正可负，负数就按64位去遍历即可）， 输出该整数的二进制包含1的个数
def count_num_one(num):
    if num<0:
        num+=2**64
    # result=''
    # while num!=0:
    #     current=num%2
    #     num//=2
    #     result+=str(current)
    # count=0
    # for i in result[::-1]:
    #     if i=='1':
    #         count+=1
    # return count
    flag=1
    count=0
    while flag<=2**63:
        if flag&num:
            count+=1
        flag<<=1
    return count


num=int(input('请输入:'))
print(count_num_one(num))

