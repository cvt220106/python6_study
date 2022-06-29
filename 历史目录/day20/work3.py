# @Author : 杨佳杰
# @Time   : 2022/6/21 20:33
# @File   : work3.py
import re

string = 'www.baidu.com....这是百度的域名abcdefg'

pattern=re.compile(r'[a-z][a-z\.]*[a-z]',re.I)
res=pattern.match(string)
if res:
    print(f'匹配成功,匹配结果为{res.group()}')
else:
    print(f'匹配失败')

