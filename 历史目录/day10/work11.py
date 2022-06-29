# @Author : 杨佳杰
# @Time   : 2022/6/9 22:02
# @File   : work11.py
import os
import time

start_time=time.time()
file=open('_The_Holy_Bible.txt','r',encoding='utf8')
num_s=0#字符数
num_row=0#行数
num_word=0#单词数
dic={}#记录单词词频
while True:
    txt=file.readline()
    if not txt:
        break
    num_s+=len(txt)
    num_row+=1
    if txt.isspace():
        continue
    current=txt.split(' ')
    for item in current:
        if item=='' or item=='\n':
            continue
        num_word+=1
        dic[item]=dic.get(item,0)+1
print(f'文件中,字符数为{num_s},行数{num_row},单词数{num_word}')
res=sorted(dic.items(),key= lambda x:x[1],reverse=True)

print('词频最高的前10个单词及词频')
print('{:^6}\t{:^6}'.format('单词','词频'))
for i in range(10):
    print(f'{res[i][0]:^6}\t{res[i][1]:^6}')
end_time=time.time()
print(f'程序运行用时{(end_time-start_time)*1000:.1f}ms')
