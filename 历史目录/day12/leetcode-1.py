# @Author : 杨佳杰
# @Time   : 2022/6/11 20:44
# @File   : leetcode-1.py
hashmap={}
list1=[1,2,3,1,2,3]
for index,item in enumerate(list1):
    if hashmap.get(item, []):
        hashmap[item].append(index)
    else:
        hashmap[item]=hashmap.get(item, [index])
if hashmap.get(4,[]):
    print(hashmap[3])
else:
    print('q')
print(hashmap[3][0])