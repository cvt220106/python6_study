# @Author : 杨佳杰
# @Time   : 2022/6/21 18:25
# @File   : work1.py
import re
name_list=['Willer Simth','Mary,Swift','T,Swift','Y jack','Jsmith']

pattern=re.compile(r'\w+[,| ]\w+$',re.I)
for name in name_list:
    res=pattern.match(name)
    if res:
        print(f'{name}匹配成功')
    else:
        print(f'{name}匹配失败')
