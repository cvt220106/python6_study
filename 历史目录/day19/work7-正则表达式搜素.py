# @Author : 杨佳杰
# @Time   : 2022/6/20 21:47
# @File   : work7-正则表达式搜素.py
import re

lst = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
for string in lst:
    res=re.match('^[bh][aiu]t$',string)
    if res:
        print(f"匹配后的结果是{res.group()}" )
    else:
        print(f'{string}匹配失败!')