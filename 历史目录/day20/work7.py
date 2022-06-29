# @Author : 杨佳杰
# @Time   : 2022/6/21 22:00
# @File   : work7.py
import re

string = '''xiaowang@163.com
xiaoming@qq.com
xiaoli@gmail.com
'''
lst = string.splitlines()
print(lst)
for item in lst:
    res = re.sub(r'[^@]+@', '1564851464@', item)
    res = re.sub(r'@.*\.','@qq.',res)
    print(res)
