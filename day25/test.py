# @Author : 杨佳杰
# @Time   : 2022/6/26 11:40
# @File   : test.py
# nums1=[28,34,38,14,30,31,23,7,28,3]
# nums2=[42,35,7,6,24,30,14,21,20,34]
nums1=[60,60,60]
nums2=[10,90,10]
sub=[0]*len(nums1)
k=0
for i,j in zip(nums1,nums2):
    sub[k]=j-i
    k+=1
dp1=[0]*len(sub)
dp1[0]=sub[0]
for i in range(1,len(sub)):
    dp1[i]=max(dp1[i-1]+sub[i],sub[i])
dp2=[0]*len(sub)
dp2[0]=sub[0]
for i in range(1,len(sub)):
    dp2[i]=min(dp2[i-1]+sub[i],sub[i])
print(max(dp1),min(dp2))
print(max(sum(nums1)+max(dp1),sum(nums2)-min(dp2)))

edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
n=5
g = [[] for _ in range(n)]
for x, y in edges:
    print(x,y)
    g[x].append(y)
    g[y].append(x)
print(g)

s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
hashmap={}
for c in s:
    hashmap[c]=hashmap.get(c,0)+1
max_odd=0
res=0
for value in hashmap.values():
    if value%2==0:
        print(value)
        res+=value
    else:
        res+=value-1
print(res+1,hashmap)

print('hello world')
