# @Author : 杨佳杰
# @Time   : 2022/6/21 20:54
# @File   : work5.py
import re
string='''helloworld
1552116**
112asasd5
********
-----123
1564---
'''

pattern=re.compile(r'[0-9a-z]+',re.I)
lst=string.splitlines()
for item in lst:
    res=pattern.search(item)
    if res:
        print(f'匹配成功,匹配结果为{res.group()}')
    else:
        print(f'匹配失败')