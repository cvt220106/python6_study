# @Author : 杨佳杰
# @Time   : 2022/6/4 22:09
# @File   : work7.py
def find_most_num(lst):
    n=len(lst)
    dic={}
    for i in lst:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for item in dic:
        if dic[item]>n/2:
            return item


def find_most_num2(lst):
    vote_num=0
    winner=lst[0]
    for i in lst:
        if vote_num==0:
            winner=i
        if i==winner:
            vote_num+=1
        else:
            vote_num-=1
    return winner


list1=[1,1,2,3,1,3,1,1,1]
print(find_most_num(list1))
print(find_most_num2(list1))






