# @Author : 杨佳杰
# @Time   : 2022/6/10 0:10
# @File   : judge.py
import time
import os

start_time = time.time()
f1=open('The_Holy_Bible.txt','r',encoding='utf-8')
f2=open('_The_Holy_Bible.txt','r',encoding='utf-8')
bool=True
while True:
    t1=f1.readline()
    t2=f2.readline()
    if not t1 or not t2:
        break
    if t1!=t2:
        bool=False
        break
if bool:
   print('相同')
else:
    print('不同')

end_time = time.time()
print(f'程序耗时{(end_time - start_time) * 1000:.1f}ms')
