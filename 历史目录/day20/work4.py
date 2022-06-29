# @Author : 杨佳杰
# @Time   : 2022/6/21 20:37
# @File   : work4.py
import re

string = '134685489674963163这是我乱打的数字'

pattern=re.compile(r'(^[\d]+)')
res=pattern.match(string)
if res:
    print(f'匹配成功,匹配结果为{res.group(1)}')
else:
    print(f'匹配失败')

