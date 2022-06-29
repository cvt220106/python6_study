# @Author : 杨佳杰
# @Time   : 2022/6/21 21:28
# @File   : work6.py
import re
string='hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分'

pattern=re.compile(r'\d{4}(?:/|年)[01]?[0-9](?:/|月)[1-3]?[0-9](?:\s|日)(?:0[0-9]|1[0-9]|2[0-4])(?::|时)[0-5][0-9](?:|分)')
res=pattern.findall(string)
if res:
    print(res)
else:
    print('匹配失败')