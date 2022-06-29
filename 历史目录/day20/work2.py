# @Author : 杨佳杰
# @Time   : 2022/6/21 20:13
# @File   : work2.py
import re
name_list=['http://www.yahoo.com',
           'https://docs.python.org',
           'https://zhuanlan.zhihu.com',
           'http://www.yahoo.net',
           'http://www.yahoo.com1']

pattern=re.compile(r'w{3}\.[^.]+\.(com|net|org)$')
for name in name_list:
    res=pattern.search(name)
    if res:
        print(f'{name}匹配成功,匹配结果为{res.group()}')
    else:
        print(f'{name}匹配失败')
