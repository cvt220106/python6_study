# @Author : 杨佳杰
# @Time   : 2022/6/14 0:59
# @File   : 7-多级排序.py
s = 'bbaa aasdadbbbddcccc'
hashmap = {}
for i in s:
    hashmap[i] = hashmap.get(i, 0) + 1
print(hashmap)
dct = sorted(sorted(hashmap.items(), key=lambda x: x[0]), key=lambda y: y[1], reverse=True)
print(dct)
current = sorted(hashmap.items(), key=lambda x: x[0])
print(current)
print(sorted(current, key=lambda x: x[1], reverse=True))
c2 = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
print(c2)
print(sorted(c2, key=lambda x: x[0]))
